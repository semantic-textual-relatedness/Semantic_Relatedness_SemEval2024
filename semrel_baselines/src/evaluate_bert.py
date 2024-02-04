from transformers import AutoTokenizer, AutoModel
import pandas as pd
import os
import json
import torch
from argparse import ArgumentParser
from scipy.stats import spearmanr
from typing import List
from sklearn.metrics.pairwise import paired_cosine_distances


# Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(
    model_output: torch.Tensor, attention_mask: torch.Tensor
) -> torch.Tensor:
    token_embeddings = model_output.last_hidden_state

    input_mask_expanded = (
        attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    )
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(
        input_mask_expanded.sum(1), min=1e-9
    )


def get_embeddings(model_name: str, sentences: List[str]) -> torch.Tensor:

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        model_output = model(**inputs)
    embeddings = mean_pooling(model_output, inputs["attention_mask"])
    return embeddings


def evaluate_embeddings(
    embeddings1: torch.Tensor, embeddings2: torch.Tensor, scores: List[float]
) -> float:
    cosine_scores = 1 - paired_cosine_distances(embeddings1, embeddings2)
    cosine_scores = cosine_scores.flatten().tolist()
    spearman_correlation = spearmanr(cosine_scores, scores)[0]
    return spearman_correlation


def main():
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument("--dataset_dir", type=str, default="STS-B")
    parser.add_argument("--model_name", type=str, default="xlm-roberta-base")
    parser.add_argument("-embedding_type", type=str, default="bert")

    args = parser.parse_args()
    model_name = args.model_name
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

    assert len(sentence_1s) == len(sentence_2s)
    assert len(sentence_1s) == len(scores)

    embedding1 = get_embeddings(model_name, sentence_1s)
    embedding2 = get_embeddings(model_name, sentence_2s)
    spearman_correlation = evaluate_embeddings(embedding1, embedding2, scores)

    if "/" in model_name:
        model_name = model_name.split("/")[1]

    result_path = os.path.join(results_dir, f"{lang_name}_{model_name}.json")

    # dump spearman_correlation, model_name, lang_name to json file
    result_dict = {
        "spearman_correlation": spearman_correlation,
        "model_name": model_name,
        "lang_name": lang_name,
        "number_samples": len(sentence_1s),
    }
    with open(result_path, "w") as f:
        json.dump(result_dict, f)


if __name__ == "__main__":
    main()


LANG_CODES = {
    "arq": "Algerian Arabic",
    "amh": "Amharic",
    "afr": "Afrikaans",
    "ary": "Moroccan Arabic",
}
