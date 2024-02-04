#!/bin/bash

# List of languages
# languages=("amh" "arb" "arq" "ary" "esp" "hau" "hin" "ind" "kin" "mar" "pan" "tel" "amh" "eng")
# languages=("mar" "pan" "tel" "hin" "eng")
# languages=("amh" "hau" "kin" "eng" "arb")
# languages=("tel" "amh")
# languages=("pan" "ind" "hau")
# languages=("eng")
# Loop through the languages
languages=("eng")
# model_names=("aubmindlab/bert-base-arabert" "UBC-NLP/MARBERT" "asafaya/bert-base-arabic")
# model_names=("alger-ia/dziribert")
# model_names=("uhhlt/am-roberta")
# model_names=("Davlan/xlm-roberta-base-finetuned-hausa")
model_names=("bert-base-uncased")
# model_names=("dccuchile/bert-base-spanish-wwm-cased" "dccuchile/albert-base-spanish" "PlanTL-GOB-ES/roberta-base-bne")
for model_name in "${model_names[@]}"
do
    for lang in "${languages[@]}"
    do
        echo $lang
        echo $model_name
        python -m src.evaluate_bert --dataset_dir data/$lang --model_name $model_name

    done
done
