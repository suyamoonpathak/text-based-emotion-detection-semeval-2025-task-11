# TBED-CS779-IITK
Text Based Emotion Detection SemEval-2025 Task 11

# Results for Track A, B, and C

| **Model Name**                                                                 | **Track** | **Accuracy** | **Micro F1** | **Macro F1** | **Weighted F1** |
|-------------------------------------------------------------------------------|-----------|--------------|--------------|--------------|-----------------|
| SamLowe/roberta-base-go_emotions                                              | A         | 0.21         | 0.45         | 0.44         | 0.42            |
| cardiffnlp/twitter-roberta-large-emotion-latest                               | A         | 0.29         | 0.54         | 0.53         | 0.50            |
| Emanuel/twitter-emotion-deberta-v3-base                                       | A         | 0.16         | 0.45         | 0.40         | 0.45            |
| meta-llama/Meta-Llama-3-8B-Instruct                                           | A         | 0.24         | 0.58         | 0.59         | 0.58            |
| cardiffnlp/twitter-roberta-large-emotion-latest (Full Fine-tuning)            | A         | 0.43         | 0.60         | 0.49         | -               |
| SamLowe/roberta-base-go_emotions (Full Fine-tuning)                           | A         | 0.44         | 0.61         | 0.49         | -               |
| cardiffnlp/twitter-roberta-large-emotion-latest (Added Classifier Layer Only) | A         | 0.57         | 0.73         | 0.69         | -               |
| cardiffnlp/twitter-roberta-large-emotion-latest (Added FC Layer + Classifier) | A         | 0.62         | 0.77         | 0.75         | -               |
| cardiffnlp/twitter-roberta-large-emotion-latest (Entailment Approach)         | A         | 0.60         | 0.73         | 0.73         | -               |
| cardiffnlp/twitter-roberta-large-emotion-latest (Oversampling Method-1)       | A         | 0.59         | 0.73         | 0.73         | -               |
| cardiffnlp/twitter-roberta-large-emotion-latest (Oversampling Method-2)       | A         | **0.64**     | **0.78**     | **0.77**     | -               |
| **After Data Augmentation**                                                   |           |              |              |              |                 |
| SamLowe/roberta-base-go_emotions                                              | A         | 0.40         | 0.59         | 0.48         | 0.55            |
| cardiffnlp/twitter-roberta-large-emotion-latest                               | A         | 0.61         | 0.76         | 0.74         | 0.72            |
| Emanuel/twitter-emotion-deberta-v3-base                                       | A         | 0.24         | 0.49         | 0.44         | 0.45            |
| cardiffnlp/twitter-xlm-roberta-base-sentiment                                 | C         | **0.10**     | **0.17**     | **0.13**     | **0.15**        |

# Results for Track B

| **Model Name**                  | **Anger (Pear R.)** | **Fear (Pear R.)** | **Joy (Pear R.)** | **Sadness (Pear R.)** | **Surprise (Pear R.)** | **Average Pearson r** |
|---------------------------------|---------------------|--------------------|-------------------|-----------------------|------------------------|-----------------------|
| cardiffnlp/twitter-roberta-large-emotion-latest (with added FC layer) | 0.80               | 0.42              | 0.72              | 0.59                 | 0.52                 |  0.61                     |

