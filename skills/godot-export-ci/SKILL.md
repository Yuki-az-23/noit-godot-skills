---
name: godot-export-ci
description: Exports and ships Godot 4.x games - export presets, headless command-line exports, export templates, Windows/macOS/Linux/Web/Android/iOS specifics (4.7 wasm64 web, GABE Android builds, D3D12 default), the shader baker, PCK patches, version stamping, and GitHub Actions CI that imports, tests, and builds. Use when the user wants a build, a release pipeline, itch.io/Steam uploads, or fixes for export failures.
---

# Godot Export & CI

## Prerequisites

1. **Export templates** must match the editor version exactly (`4.7.2.stable`). Install them via Editor > Manage Export Templates, or extract the official `.tpz` to:
   - Linux: `~/.local/share/godot/export_templates/4.7.2.stable/`
   - macOS: `~/Library/Application Support/Godot/export_templates/4.7.2.stable/`
   - Windows: `%APPDATA%\Godot\export_templates\4.7.2.stable\`
2. **`export_presets.cfg`** must exist. Create the presets once in the editor (Project > Export) and commit the file. Keep secrets out of it (see Signing).
3. Run an import pass on fresh checkouts: `godot --headless --path . --import`.

## Command-Line Export

```bash
godot --headless --path . --export-release "Windows Desktop" build/windows/MyGame.exe
godot --headless --path . --export-release "Linux"           build/linux/MyGame.x86_64
godot --headless --path . --export-release "Web"             build/web/index.html
godot --headless --path . --export-debug   "Android"         build/android/MyGame.apk
godot --headless --path . --export-pack    "Linux"           build/patch.pck    # data-only PCK/patch
```
- The preset name is the `name=` in `export_presets.cfg`, and it is case-sensitive.
- The output directory must exist (`mkdir -p`).
- Exit code is non-zero on failure. Grep the output for `ERROR:` too, because some template problems only warn.

## Per-Platform Notes

| Platform | Notes |
|----------|-------|
| Windows | New 4.6+ projects default to **Direct3D 12**. Keep a Vulkan or Compatibility fallback for old GPUs (`rendering/rendering_device/driver.windows`). Use rcedit for icon and metadata (Editor Settings > Export > Windows). Code signing via `signtool` settings. |
| macOS | Notarization needs an Apple ID or API key. Build universal binaries. Unsigned builds work only with a right-click → Open warning. |
| Linux | Ship `.x86_64` (+ `.pck` unless embedded). Consider an `arm64` preset for handhelds. |
| Web | Uses the **Compatibility** renderer (WebGL 2); there is no WebGPU yet. Threads need cross-origin isolation (COOP/COEP headers). Disable "Thread Support" for itch.io and simple hosts. **4.7** adds wasm64 exports (more than 4 GB memory) for large projects. Audio starts after the first user gesture. |
| Android | Use a Gradle build for plugins and custom manifests. 4.6/4.7: **GABE** (Godot Android Build Environment) runs Gradle builds and exports directly from the Android editor. Keystores: debug is auto-generated, release is set via env vars (below). Target API level per Play Store policy. |
| iOS / visionOS | Export creates an Xcode project; build and sign in Xcode on macOS. |

## Signing Secrets via Environment Variables

Never commit keystore passwords. Godot reads these at export time:
```
GODOT_ANDROID_KEYSTORE_RELEASE_PATH
GODOT_ANDROID_KEYSTORE_RELEASE_USER
GODOT_ANDROID_KEYSTORE_RELEASE_PASSWORD
GODOT_SCRIPT_ENCRYPTION_KEY        # if you use PCK encryption (requires custom templates)
```
Store them as CI secrets.

## Shipping Hygiene

- **Shader baker (4.5+):** enable it in the export preset to precompile shaders and reduce first-run stutter. It increases export time, so enable it for release presets.
- **Exclude dev files:** set export filters to exclude `test/*`, `addons/gut/*`, `addons/gdUnit4/*`, `addons/godot_ai_bridge/*`, `*.md`. The AI Bridge plugin and its runtime autoload should **never ship**. Disable the plugin or remove the autoload in a release-only step, or guard it with `OS.has_feature("editor")`/`OS.is_debug_build()`.
- **Version stamp:** set `application/config/version` and read it with `ProjectSettings.get_setting("application/config/version")` for the title screen and bug reports.
- **Feature tags:** branch platform code with `OS.has_feature("web")`, `"mobile"`, `"steam"` (custom tag on a preset), or `"demo"`.
- **Release logging:** 4.5+ script backtraces work in release builds. Add a `Logger` subclass (4.5+) with `OS.add_logger()` to collect errors to `user://logs`.

## GitHub Actions: Test + Export

```yaml
# .github/workflows/build.yml
name: build
on: [push, pull_request]
env:
  GODOT_VERSION: "4.7.2"
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { lfs: true }
      - name: Install Godot + templates
        run: |
          base=https://github.com/godotengine/godot/releases/download/${GODOT_VERSION}-stable
          curl -sSLfo godot.zip "$base/Godot_v${GODOT_VERSION}-stable_linux.x86_64.zip"
          unzip -q godot.zip && sudo mv Godot_v${GODOT_VERSION}-stable_linux.x86_64 /usr/local/bin/godot
          curl -sSLfo tpl.tpz "$base/Godot_v${GODOT_VERSION}-stable_export_templates.tpz"
          mkdir -p ~/.local/share/godot/export_templates/${GODOT_VERSION}.stable
          unzip -q tpl.tpz -d /tmp/tpl && mv /tmp/tpl/templates/* ~/.local/share/godot/export_templates/${GODOT_VERSION}.stable/
      - name: Import
        run: godot --headless --path . --import
      - name: Tests (GUT)
        if: hashFiles('addons/gut/plugin.cfg') != ''
        run: godot --headless --path . -s addons/gut/gut_cmdln.gd -gdir=res://test -ginclude_subdirs -gexit
      - name: Export
        run: |
          mkdir -p build/linux build/windows build/web
          godot --headless --path . --export-release "Linux" build/linux/game.x86_64
          godot --headless --path . --export-release "Windows Desktop" build/windows/game.exe
          godot --headless --path . --export-release "Web" build/web/index.html
      - uses: actions/upload-artifact@v4
        with: { name: builds, path: build/ }
```
Variations:
- **GdUnit4 tests:** replace the test step with `./addons/gdUnit4/runtest.sh --godot_binary /usr/local/bin/godot --headless --ignoreHeadlessMode -a res://test`.
- **UI click tests:** prefix the test command with `xvfb-run -a` and drop `--headless`.
- **itch.io upload:** use butler with `BUTLER_API_KEY` as a secret: `butler push build/web user/game:html5`.
- **Steam:** steamcmd with a builder account and `app_build.vdf`; keep credentials in secrets.
- **C# projects:** use the .NET (mono) Godot build and templates (`..._mono_linux_x86_64.zip`, `..._mono_export_templates.tpz`), and add `actions/setup-dotnet`.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| "No export template found" | Template folder name must match `godot --version` exactly (e.g. `4.7.2.stable`). |
| Preset not found | Preset name typo, or `export_presets.cfg` not committed. |
| Exported game missing resources | Resources loaded by string path at runtime aren't detected. Add them via export filter "include" patterns, or reference them with `preload`. |
| Works in editor, crashes in export | Code reads `res://` with `DirAccess` (imported files are remapped) or writes to `res://` (read-only). Use `ResourceLoader.list_directory()` and `user://`. |
| Web build is a black screen | Check the browser console. Usually missing COOP/COEP headers with threads on, or a Forward+-only feature. |
| Huge build size | Exclude dev addons and test assets, compress textures (VRAM compressed), use OGG for music. |
