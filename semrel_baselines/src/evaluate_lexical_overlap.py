from nltk import ngrams
import os
import json
import pandas as pd
from argparse import ArgumentParser
from scipy.stats import spearmanr


def calculate_dice_coefficient(sentence1: str, sentence2: str) -> float:
    n = 1
    ngram1 = ngrams(sentence1.split(), n)
    ngram2 = ngrams(sentence2.split(), n)
    ngram1 = set(ngram1)
    ngram2 = set(ngram2)
    overlap = 2 * len(ngram1.intersection(ngram2))
    return overlap / (len(ngram1) + len(ngram2))


def main():
    parser = ArgumentParser()
    parser.add_argument("--dataset_dir", type=str, default="STS-B")
    parser.add_argument("-data_split", type=str, default="test")
    

    args = parser.parse_args()
    data_split = args.data_split
    lang_name = args.dataset_dir.split("/")[1]
    test_data_path = os.path.join(args.dataset_dir, f"{lang_name}_{data_split}.csv")
    results_dir = os.path.join("results_lexical", lang_name)
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    test_df = pd.read_csv(test_data_path)
    # spearman_correlations = []
    scores = test_df["Score"].tolist()
    scores = [float(score) for score in scores]
    sentences = test_df["Text"].tolist()
    sentence_1s = []
    sentence_2s = []
    for sentence in sentences:
        sentence_1, sentence_2 = sentence.split(
            "\t"
        )  # this shall be fixed after the format for pan, ind and Hau
        sentence_1s.append(sentence_1)
        sentence_2s.append(sentence_2)

    lexical_overlap_scores = []
    for sent1, sent2 in zip(sentence_1s, sentence_2s):
        lexical_overlap_scores.append(calculate_dice_coefficient(sent1, sent2))

    spearman_correlation, _ = spearmanr(scores, lexical_overlap_scores)
    result_dict = {
        "spearman_correlation": spearman_correlation,
        "metric": "lexical_overlap",
        "lang_name": lang_name,
        "number_samples": len(sentence_1s),
    }
    result_path = os.path.join(results_dir, f"{lang_name}_lexical_overlap.json")
    with open(result_path, "w") as f:
        json.dump(result_dict, f)


if __name__ == "__main__":
    main()
