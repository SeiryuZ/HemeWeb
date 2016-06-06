#! /bin/bash

pandoc ../proposal/README.md -f markdown -t latex -s -o IRP.tex
sed -i '' 's/htbp/H/g' IRP.tex

sed -i '' -e '3i\
\\usepackage[margin=1in]{geometry}' IRP.tex


sed -i '' -e '3i\
\\usepackage{float}' IRP.tex
