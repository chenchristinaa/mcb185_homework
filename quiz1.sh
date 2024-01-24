# Authors: Christina Chen, Alexandria Skinner

echo "Christina Chen"
echo "$USER"

gunzip -c ../MCB185/data/dictionary.gz | grep "a" | grep -v "[^muocfta]" | grep -E ".{4,100}"

gunzip -c ../MCB185/data/dictionary.gz | grep "b" | grep -v "[^tairnlb]" | grep -E ".{4,100}"

gunzip -c ../MCB185/data/dictionary.gz | grep "c" | grep -v "[^maodinc]" | grep -E ".{4,100}"

gunzip -c ../MCB185/data/dictionary.gz | grep "z" | grep -v "[^anoigrz]" | grep -E ".{4,100}"

gunzip -c ../MCB185/data/jaspar2024_core.transfac.gz | grep "tax_group" | cut -c "14-100" | sort | uniq -c | sort -n