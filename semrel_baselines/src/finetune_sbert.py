from sentence_transformers import SentenceTransformer, InputExample, losses, evaluation
from torch.utils.data import DataLoader
import os
import pandas as pd
from argparse import ArgumentParser
from typing import List


def create_train_dataset(
    dataset_dir: str, list_of_langs: List[str]
) -> List[InputExample]:

    train_examples = []
    for lang in list_of_langs:
        train_data_path = os.path.join(dataset_dir, lang, f"{lang}_train.csv")
        if not os.path.exists(train_data_path):
            print(f"Train data for {lang} does not exist")
            continue

        train_df = pd.read_csv(train_data_path)
        scores = train_df["Score"].tolist()
        scores = [float(score) for score in scores]
        sentences = train_df["Text"].tolist()
        sentence_1s = []
        sentence_2s = []
        for sentence in sentences:
            sentence_1, sentence_2 = sentence.split("\n")
            sentence_1s.append(sentence_1)
            sentence_2s.append(sentence_2)
        for i in range(len(scores)):
            train_examples.append(
                InputExample(texts=[sentence_1s[i], sentence_2s[i]], label=scores[i])
            )
    return train_examples


def main():
    parser = ArgumentParser()
    parser.add_argument("--dataset_dir", type=str, default="data")
    parser.add_argument("--model_name", type=str, default="sentence-transformers/LaBSE")
    dataset_dir = parser.parse_args().dataset_dir
    model_name = parser.parse_args().model_name
    list_of_langs = ["esp"]
    train_examples = create_train_dataset(dataset_dir, list_of_langs)
    train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)
    model = SentenceTransformer(model_name, device="cuda")
    loss_function = losses.CosineSimilarityLoss(model=model)
    model.fit(
        train_objectives=[(train_dataloader, loss_function)],
        epochs=10,
        warmup_steps=100,
        output_path="semrel_baselines/models/finetuned_esp_labse",
    )


if __name__ == "__main__":
    main()
