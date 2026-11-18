#!/usr/bin/env bash
# Rebuild the annotated feature-flow GIF from the approved static social-preview image.
# Requires ImageMagick with GIF and JPEG support.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
base="$tmp/base.png"
convert "$root/assets/social-preview.jpg" -resize 1100x550! "$base"
texts=(
  '01  CAPTURE PAGE EVIDENCE  |  Use the page content Clipper supplies'
  '02  SELECT A JSON TEMPLATE  |  Choose fields, callouts, and source position'
  '03  RUN INTERPRETER MANUALLY  |  Review the generated explanation yourself'
  '04  KEEP THE ORIGINAL SOURCE  |  Save the supplied content with the Markdown note'
  '05  CONNECT YOUR KNOWLEDGE  |  Review the note, then organize it in your vault'
)
boxes=('70,130 345,400' '355,180 525,390' '515,95 790,420' '515,95 790,420' '820,130 1070,420')
for i in 0 1 2 3 4; do
  convert "$base" \
    -fill 'rgba(9,8,20,0.86)' -draw 'roundrectangle 18,452 1082,532 18,18' \
    -fill '#9bead0' -font DejaVu-Sans-Bold -pointsize 18 -gravity northwest -annotate +38+468 "${texts[$i]}" \
    -stroke '#a890fa' -strokewidth 5 -fill 'rgba(153,129,248,0.16)' -draw "roundrectangle ${boxes[$i]} 22,22" \
    -stroke '#91eed7' -strokewidth 2 -fill none -draw "roundrectangle ${boxes[$i]} 22,22" \
    -quality 82 "$tmp/frame-$i.jpg"
done
convert -delay 130 "$tmp/frame-0.jpg" "$tmp/frame-1.jpg" "$tmp/frame-2.jpg" "$tmp/frame-3.jpg" -delay 200 "$tmp/frame-4.jpg" -loop 0 "$root/assets/feature-flow.gif"
