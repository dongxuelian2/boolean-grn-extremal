#!/usr/bin/env python3
"""Package own manuscript/source/audits only; never includes downloaded papers."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED


def main():
    root = Path(__file__).resolve().parents[1]
    pdf = root / "output/manuscript/grn-extremal-manuscript.pdf"
    if not pdf.exists():
        raise SystemExit("Run bash scripts/build_manuscript.sh first")
    paths = []
    for directory in ["manuscript", "submission", "scripts", "tests", "docs/research"]:
        paths.extend(p for p in (root/directory).rglob("*")
                     if p.is_file() and p.suffix in {".tex", ".md", ".txt", ".py", ".sh"}
                     and "__pycache__" not in p.parts)
    paths.extend(root/p for p in ["README.md", "RESEARCH.md"])
    out = root / "output/submission"
    out.mkdir(parents=True, exist_ok=True)
    archive = out / "grn-extremal-manuscript-package.zip"
    manifest = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(paths)}
    with ZipFile(archive, "w", ZIP_DEFLATED) as z:
        for p in sorted(paths):
            z.write(p, p.relative_to(root))
        z.write(pdf, "manuscript.pdf")
        z.writestr("source-manifest.json", json.dumps(manifest, indent=2)+"\n")
    with ZipFile(archive) as z:
        assert z.testzip() is None
        assert not any(x.startswith(".git/") or "__pycache__" in x for x in z.namelist())
    print(f"Created {archive} ({len(paths)} source files, PDF and SHA256 manifest)")


if __name__ == "__main__":
    main()
