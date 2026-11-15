#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p output/pdf
pandoc docs/research/eventual_extremal_classification.md \
  --from markdown+tex_math_single_backslash --standalone \
  --pdf-engine=xelatex -V geometry:margin=1in -V fontsize=11pt \
  -V colorlinks=true -V urlcolor=blue \
  -o output/pdf/eventual-extremal-classification.pdf
