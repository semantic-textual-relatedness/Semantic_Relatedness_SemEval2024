# SemRel Task Baselines

## How to run the baselines?

1. Create a virtualenv or a conda env and install the requirements residing in the `requirements.txt`
2. You can then refer to various bash scripts residing in the scripts folder to calculate/finetune various baselines.
3. Make sure you have your datasets residing in the `data` folder. Format of the language data directory should be: `data/{lang_name}/{lang_name}_{data_split}.csv` where your data_split is `test` or `val`.
4. You can have a look at the respective python scripts in the `src` directory to know more about supported arguments.