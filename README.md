# TBED-CS779-IITK
Text Based Emotion Detection SemEval-2025 Task 11

## Track A:
### 1) Notebook: twitterRobertaLarge.ipynb
This notebook shows the code to predict the multiemotion labels of Track A training Dataset without finetuning. The model used was cardiffnlp/twitter-roberta-large-emotion-latest available on huggingface. The model predicts 11 emotions out of which 5 required emotion labels are selected as prediction.

### 2) Notebook: trainTwitterRoberta_accuracy.ipynb
This notebook contains the code of full finetuning of cardiffnlp/twitter-roberta-large-emotion-latest model. The model predicts 11 emotions out of which 5 required emotion labels are selected as prediction.

### 3) Notebook: traintwitterRobertaAddingFCLayer.ipynb
This notebook contains the code of finetuning the last added FC layer of cardiffnlp/twitter-roberta-large-emotion-latest Classifier layer. Since the base model prediction was for 11 labels, we have added an FC layer with 5 desired emotion labels and train only this layer freezing the base model.

### 4) Notebook: trainClassifierHeadtwitterRobertaAddingFCLayer.ipynb
This notebook shows the code of finetuning the last added FC layer along with the Classifier layer (two FC layer at the last) of cardiffnlp/twitter-roberta-large-emotion-latest Classifier layer. Since the base model prediction was for 11 labels, we have added an FC layer with 5 desired emotion labels and train only this layer freezing the base model.

### 5) Notebook: AUGMENTED_trainGoEmotionsRoberta_accuracy.ipynb
This notebook shows the code of finetuning the last added FC layer along with the Classifier layer (two FC layer at the last) of cardiffnlp/twitter-roberta-large-emotion-latest Classifier layer. Synthetic points were generated to overcome the imbalanced class distribution. ChatGPT 4o was used to create new data points.

### 6) Notebook: EnatailmentApproachtrainClassifierHeadtwitterRobertaAddingFCLayer.ipynb
This code trains the last added FC layer along with the Classifier layer (two FC layer at the last) of cardiffnlp/twitter-roberta-large-emotion-latest Classifier layer on entailment dataset obtained by converting raw data to 'Premise' and 'Hypothesis'. Here also base model weights was from except Classfier layers.
Example:

Original Sample:<br>
'Text':  'But not very happy.'<br>
Labels: [0.0, 0.0, 1.0, 1.0, 0.0]  ('Anger','Fear','Joy','Sadness','Surprise')

Converted to:<br>
'Premise':  'But not very happy.'<br>
'Hypothesis': 'The speaker is feeling Anger'<br>
Labels: [0.0] (Neutral or Contradiction

And likewise for other emotions.

### 7) Notebook: BalMinoritytrainClassifierHeadtwitterRobertaAddingFCLayer.ipynb
This code trains the last added FC layer along with the Classifier layer (two FC layer at the last) of cardiffnlp/twitter-roberta-large-emotion-latest Classifier layer on balanced obtained by oversampling the minortity class with oversampling. The base model weights was from except Classfier layers.<br>
Oversampling Method-1: Selected the class with lowest representation and selected those samples which have 1 in the that emotion label and all others 0. We randomly sampled 100 samples from it and then again checked for lowest class representations and repeated the procedure till we got balanced samples

### 8) Notebook: BalMinority2trainClassifierHeadtwitterRobertaAddingFCLayer.ipynb
This code trains the last added FC layer along with the Classifier layer (two FC layer at the last) of cardiffnlp/twitter-roberta-large-emotion-latest Classifier layer on balanced obtained by oversampling the minortity class with oversampling. The base model weights was from except Classfier layers.<br>
Oversampling Method-2: Selected the class with lowest representation and sampled those rows which do not have 1 in the majority label class (like Anger which had 1611 samples). We randomly sampled 100 samples from it and then again checked for lowest class representations and repeated the procedure till we got balanced samples

## Track B:
### 1) Notebook: TrackBtrainClassifierHeadtwitterRobertaAddingFCLayer.ipynb
This notebook shows the code of finetuning the last added FC layer along with the Classifier layer (two FC layer at the last) of cardiffnlp/twitter-roberta-large-emotion-latest Classifier layer. Since the base model prediction was for 11 labels, we have added an FC layer with 5 desired emotion labels and train only this layer freezing the base model.<br>
Since the base model was trained on dataset with 0/1 labels and ours was an intensity prediction problem, we first converted the intensities into range 0 to 1 with the following rule:<br>
label-0: 0.0<br> 
label-1: 0.6<br>
label-2: 0.75<br>
label-3: 1.0<br>
After prediction the score was reconverted to desired labels with another set of rules as follows: <br>
Score< 0.5: label-0<br>
0.5 <= Score < 0.7: label-1<br>
0.7 <= Score < 0.8: label-2<br>
0.8 <= Score <= 1.0: label-3<br>

## Track C:
### 1) Notebook: dataset_XED_train_trackC.ipynb
To assess the compatibility of XED for the purpose of integration, empirical performance comparison is done using trained models.The XED dataset was utilized for fine tuning the best-performing model (cardiffnlp/twitter-roberta-large-emotion-latest)from the original dataset. The model trained achieved comparable accuracy with a F1-score of 0.540793.

### 2) Notebook: dataset_XED_similarity_score.ipynb
We explored the possibility of data augmentation through the integration of external datasets. The XED dataset annotated using Plutchik’s 8 core emotions iz evaluated for this purpose. The approach involved similarity analysis between datasets. Similarity score between the two datasets is computed to be 0.26, indicating a moderate level of similarity between the two.

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

