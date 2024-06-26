# SemEval 2024 Task 1: Semantic Textual Relatedness for African and Asian Languages

This repository contains the data and resources for the SemEval 2024 Task 1: Semantic Textual Relatedness (STR). For more information, please visit the [shared task and competition websites](https://semantic-textual-relatedness.github.io).

[Dataset](https://github.com/semantic-textual-relatedness/Semantic_Relatedness_SemEval2024#dataset) | 
[Languages](https://github.com/semantic-textual-relatedness/Semantic_Relatedness_SemEval2024#languages) | 
[Shared Task Starter Kit](https://github.com/semantic-textual-relatedness/Semantic_Relatedness_SemEval2024#shared-task-starter-kit) | 
[Citing This Work](https://github.com/semantic-textual-relatedness/Semantic_Relatedness_SemEval2024#citing-this-work)

If you use our data, please cite our papers:

```bibtex
@inproceedings{ousidhoum2024semrel2024,
title={SemRel2024: A Collection of Semantic Textual Relatedness Datasets for 13 Languages}, 
author={Ousidhoum, Nedjma and Muhammad, Shamsuddeen Hassan and Abdalla, Mohamed and Abdulmumin, Idris and Ahmad, Ibrahim Said and
Ahuja, Sanchit and Aji, Alham Fikri and Araujo, Vladimir and Ayele, Abinew Ali and Baswani, Pavan and Beloucif, Meriem and Biemann, Chris and Bourhim, Sofia and De Kock, Christine and Dekebo, Genet Shanko and
Oumaima Hourrane and Gopichand Kanumolu and Lokesh Madasu and Samuel Rutunda and Manish Shrivastava and Solorio, Thamar and Surange, Nirmal and Tilaye, Hailegnaw Getaneh and Vishnubhotla, Krishnapriya and Winata, Genta and Yimam, Seid Muhie and Mohammad, Saif M.},
booktitle = "Findings of the Association for Computational Linguistics: ACL 2024",
year = "2024",
publisher = "Association for Computational Linguistics",
}

@inproceedings{ousidhoum-etal-2024-semeval, 
title = "{S}em{E}val-2024 Task 1: Semantic Textual Relatedness for African and Asian Languages",
author = "Ousidhoum, Nedjma and Muhammad, Shamsuddeen Hassan and Abdalla, Mohamed and Abdulmumin, Idris and
Ahmad,Ibrahim Said and Ahuja, Sanchit and Aji, Alham Fikri and Araujo, Vladimir and     Beloucif, Meriem and
De Kock, Christine and Hourrane, Oumaima and Shrivastava, Manish and Solorio, Thamar and Surange, Nirmal and
Vishnubhotla, Krishnapriya and Yimam, Seid Muhie and Mohammad, Saif M.",
booktitle = "Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)",
year = "2024",
publisher = "Association for Computational Linguistics"
}
```
The annotation guidelines are available here. (The PDF named SemRel Annotation guidelines.)

Check the SemRel Baseline Folder for details about the [baseline experiment.](https://github.com/semantic-textual-relatedness/Semantic_Relatedness_SemEval2024/tree/main/semrel_baselines) 


## Languages

The STR task focuses on the following 14 languages:


1. Afrikaans (_afr_ released)
2. Algerian Arabic (_arq_ released)
3. Amharic (_amh_ released)
4. English (_eng_ released)
5. Hausa (_hau_ released)
6. Indonesian (_ind_ released)
7. Hindi (_hin_ released)
8. Kinyarwanda (_kin_ released)
9. Marathi (_mar_ released)
10. Modern Standard Arabic (_arb_ released)
11. Moroccan Arabic (_ary_ released)
12. Punjabi (_pan_ released)
13. Spanish (_esp_ released)
14. Telugu (_tel_ released)

## Contact Information 
If you need additional information about a specific dataset, see below.

- For questions about the Afrikaans dataset, please contact Christine de Kock.
- For questions about the Algerian Arabic and Modern Standard datasets, please contact Nedjma Ousidhoum and Meriem Beloucif.
- For questions about the Amharic dataset, please contact Seid Muhie Yimam.
- For questions about the Moroccan Arabic dataset, please contact Oumaima Hourrane.
- For questions about the English dataset, please contact Krishnapriya Vishnubhotla, Mohamed Abdalla, and Saif M. Mohammad.
- For questions about the Hausa and Kinyarwanda datasets, please contact Shamsuddeen Hassan Muhammad, Idris Abdulmumin, and Ibrahim Said Ahmad.
- For questions about the Hindi, Marathi, and Telugu datasets, please contact Nirmal Surange and Manish Shrivastava.
- For questions about the Indonesian dataset, please contact Alham Fikri Aji.
- For questions about the Punjabi dataset, please contact Sanchit Ahuja.
- For questions about the Spanish dataset, please contact Vladimir Araujo and Thamar Solorio.

## Dataset

The STR dataset is available in the data folder or can be downloaded from [Hugging Face](https://huggingface.co/datasets/SemRel/SemRel2024).

- For Track  A: [TrackA folder](https://github.com/semantic-textual-relatedness/Semantic_Relatedness_SemEval2024/tree/main/Track%20A)
- For Track  B: [TrackB folder](https://github.com/semantic-textual-relatedness/Semantic_Relatedness_SemEval2024/tree/main/Track%20B)
- For Track  C: [TrackC folder](https://github.com/semantic-textual-relatedness/Semantic_Relatedness_SemEval2024/tree/main/Track%20C)

**Note that the full BWS tuple annotations cabe found in the BWS folder.**


## Shared Task Starter Kit

A starter kit is available to help you create a baseline result. You can open the starter kit in a Colab Notebook and run the baseline system. The resultant experiment can be submitted to Codalab to ensure the submission format is clear.

To run the Colab Notebook, click the badge "Open in Colab".


- **Simple Co-occurrence Baseline for Semantic Relatedness**: <a target="_blank" href="https://colab.research.google.com/github/shmuhammadd/semantic_relatedness/blob/main/Simple_English_Baseline_v2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


## SemRel Related Papers.

- [STR dataset paper](https://arxiv.org/abs/2402.08638)
- [STR SemEval task description paper](https://arxiv.org/pdf/2403.18933.pdf)

