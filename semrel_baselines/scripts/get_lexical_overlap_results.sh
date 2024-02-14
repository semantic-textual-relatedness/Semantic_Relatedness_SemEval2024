#!/bin/bash

# List of languages
# languages=("eng" "amh" "arb" "arq" "ary" "esp" "hau" "hin" "ind" "kin" "mar" "pan" "tel" "afr")
# languages=("tel" "amh")
languages=("afr")
# languages=("pan" "ind" "hau")
# Loop through the languages
for lang in "${languages[@]}"
do
    echo "Running evaluate_lexical_overlap for $lang"
    python -m src.evaluate_lexical_overlap --dataset_dir data/$lang
done