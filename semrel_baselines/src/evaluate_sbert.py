from sentence_transformers import (
    SentenceTransformer,
)
from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator

from argparse import ArgumentParser
import os
import pandas as pd


def main():
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument("--dataset_dir", type=str, default="STS-B")
    parser.add_argument("--model_name", type=str, default="sentence-transformers/LaBSE")
    parser.add_argument("-embedding_type", type=str, default="sentence_bert")

    args = parser.parse_args()
    model_name = args.model_name
    embedding_type = args.embedding_type

    lang_name = args.dataset_dir.split("/")[1]
    test_data_path = os.path.join(args.dataset_dir, f"{lang_name}_test.csv")
    results_dir = os.path.join("results", lang_name)
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
            "\n"
        )  # this shall be fixed after the format for pan, ind and Hau
        sentence_1s.append(sentence_1)
        sentence_2s.append(sentence_2)
    if "/" in model_name:
        tmp_model_name = model_name.split("/")[1]
    result_path = os.path.join(results_dir, f"{lang_name}_{tmp_model_name}.csv")
    if os.path.exists(result_path):
        # delte the file
        os.remove(result_path)

    evaluator = EmbeddingSimilarityEvaluator(
        sentence_1s,
        sentence_2s,
        scores,
        name=f"{lang_name}_test_{tmp_model_name}",
        show_progress_bar=True,
    )

    model = SentenceTransformer(model_name)
    model.evaluate(evaluator, output_path=results_dir)


if __name__ == "__main__":
    main()
