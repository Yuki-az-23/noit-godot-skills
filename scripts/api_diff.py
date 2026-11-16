# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 noit2.com — part of noit-godot-skills
"""Diff Godot class-reference XML between releases.

Usage: python3 -I api_diff.py <docs_root> <tag1> <tag2> [...] > out.md
Each <docs_root>/<tag> holds doc/classes/*.xml and modules/*/doc_classes/*.xml.
Outputs a markdown changelog of added/removed/deprecated classes and members.
"""
import sys, os, glob
import xml.etree.ElementTree as ET


def load(root):
    classes = {}
    for path in glob.glob(os.path.join(root, "**", "*.xml"), recursive=True):
        try:
            el = ET.parse(path).getroot()
        except ET.ParseError:
            continue
        if el.tag != "class":
            continue
        name = el.get("name")
        info = {
            "inherits": el.get("inherits", ""),
            "deprecated": el.get("deprecated") is not None,
            "experimental": el.get("experimental") is not None,
            "brief": (el.findtext("brief_description") or "").strip().split("\n")[0],
            "members": {},
        }
        for kind, xp, tag in (
            ("method", "methods/method", "method"),
            ("property", "members/member", "member"),
            ("signal", "signals/signal", "signal"),
            ("constant", "constants/constant", "constant"),
            ("annotation", "annotations/annotation", "annotation"),
        ):
            for m in el.findall(xp):
                mname = m.get("name")
                sig = mname
                if kind in ("method", "signal", "annotation"):
                    args = []
                    for p in m.findall("param"):
                        a = f"{p.get('name')}: {p.get('type')}"
                        if p.get("default") is not None:
                            a += f" = {p.get('default')}"
                        args.append(a)
                    ret = m.find("return")
                    sig = f"{mname}({', '.join(args)})"
                    if ret is not None and ret.get("type") not in (None, "void"):
                        sig += f" -> {ret.get('type')}"
                elif kind == "property":
                    sig = f"{mname}: {m.get('type')}"
                elif kind == "constant" and m.get("enum"):
                    sig = f"{m.get('enum')}.{mname}"
                key = (kind, mname if kind != "constant" else sig)
                info["members"][key] = {
                    "sig": sig,
                    "deprecated": m.get("deprecated") is not None,
                }
        classes[name] = info
    return classes


def fmt_member(kind, sig):
    return f"`{sig}`" if kind != "property" else f"`{sig}` (property)"


def diff(a, b, ta, tb):
    out = [f"\n## {ta} → {tb}\n"]
    new = sorted(set(b) - set(a))
    gone = sorted(set(a) - set(b))
    newly_dep = sorted(c for c in set(a) & set(b) if b[c]["deprecated"] and not a[c]["deprecated"])
    if new:
        out.append(f"### New classes ({len(new)})\n")
        for c in new:
            flag = " *(experimental)*" if b[c]["experimental"] else ""
            out.append(f"- **{c}** ← {b[c]['inherits'] or '—'}{flag}: {b[c]['brief']}")
        out.append("")
    if gone:
        out.append(f"### Removed classes ({len(gone)})\n")
        out += [f"- {c}" for c in gone] + [""]
    if newly_dep:
        out.append(f"### Newly deprecated classes ({len(newly_dep)})\n")
        out += [f"- {c}" for c in newly_dep] + [""]
    changed = []
    for c in sorted(set(a) & set(b)):
        ma, mb = a[c]["members"], b[c]["members"]
        added = [k for k in mb if k not in ma]
        removed = [k for k in ma if k not in mb]
        dep = [k for k in mb if k in ma and mb[k]["deprecated"] and not ma[k]["deprecated"]]
        sigchg = [k for k in mb if k in ma and k[0] in ("method", "signal") and mb[k]["sig"] != ma[k]["sig"]]
        if not (added or removed or dep or sigchg):
            continue
        lines = [f"#### {c}"]
        order = {"method": 0, "property": 1, "signal": 2, "annotation": 3, "constant": 4}
        for k in sorted(added, key=lambda k: (order[k[0]], k[1])):
            lines.append(f"- + {k[0]} {fmt_member(k[0], mb[k]['sig'])}")
        for k in sorted(sigchg, key=lambda k: (order[k[0]], k[1])):
            lines.append(f"- ~ {k[0]} `{ma[k]['sig']}` → `{mb[k]['sig']}`")
        for k in sorted(dep, key=lambda k: (order[k[0]], k[1])):
            lines.append(f"- ⚠ deprecated {k[0]} `{mb[k]['sig']}`")
        for k in sorted(removed, key=lambda k: (order[k[0]], k[1])):
            lines.append(f"- − removed {k[0]} `{ma[k]['sig']}`")
        changed.append("\n".join(lines))
    if changed:
        out.append(f"### Changed classes ({len(changed)})\n")
        out.append("\n\n".join(changed))
    return "\n".join(out)


def main():
    root, tags = sys.argv[1], sys.argv[2:]
    data = {t: load(os.path.join(root, t)) for t in tags}
    print("# Godot engine API changes " + f"({tags[0]} → {tags[-1]})")
    print("\nGenerated from the engine's own class reference XML (doc/classes and modules/*/doc_classes) at each release tag. `+` added, `~` signature changed, `⚠` newly deprecated, `−` removed.\n")
    for t in tags:
        print(f"- {t}: {len(data[t])} classes")
    for ta, tb in zip(tags, tags[1:]):
        print(diff(data[ta], data[tb], ta, tb))


if __name__ == "__main__":
    main()
