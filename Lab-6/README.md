readme_content = r"""
# DS605 Lab 06: Feature Extraction and Machine Learning with Image and Text Data

## Overview

This lab explores feature extraction from image and text data and applies
traditional machine learning algorithms to classification tasks.

The work is divided into:
- Part A: Asphalt crack image classification
- Part B: Email classification using word-count and TF-IDF representations
- Part C: Improving text classification using Complement Naive Bayes

## Part A: Asphalt Crack Image Classification

### Dataset

The image dataset contains 400 images:
- 200 crack images
- 200 non-crack images

### Feature Extraction

Images were processed using Python image-processing tools. Numerical features
include:
- Mean and standard deviation of pixel intensity
- Minimum and maximum intensity
- 16-bin intensity histogram
- Canny edge count and edge density
- Dark-pixel ratio
- Bright-pixel ratio

The resulting dataset contains 24 numerical features and one target label.

### Models and Results

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.9500 | 0.9500 | 0.9500 | 0.9500 |
| Decision Tree | 0.9375 | 0.9070 | 0.9750 | 0.9398 |

The data was split into training and testing sets using an 80:20 stratified
split with random_state=42.

### Output Files

- `asphalt_image_features.csv`
- `model_comparison.csv`
- `crack_visualization.png`
- `noncrack_visualization.png`

## Part B: Email Classification

### Dataset

The email dataset contains 5,172 rows and 3,000 existing word-count features.
The target column is `Prediction`.

Target distribution:
- Class 0: 3,672 emails
- Class 1: 1,500 emails

An 80:20 stratified train-test split was used with random_state=42.

### Models and Results

Multinomial Naive Bayes was evaluated using the existing word-count features
and a TF-IDF transformation of those features.

| Representation | Model | Accuracy | Precision | Recall | F1-score |
|---|---|---:|---:|---:|---:|
| Word Counts | Multinomial Naive Bayes | 0.9420 | 0.8681 | 0.9433 | 0.9042 |
| TF-IDF | Multinomial Naive Bayes | 0.8802 | 0.9444 | 0.6233 | 0.7510 |

### Part C: Improvement Experiment

Complement Naive Bayes was tested on the original word-count features.

| Representation | Model | Accuracy | Precision | Recall | F1-score |
|---|---|---:|---:|---:|---:|
| Word Counts | Complement Naive Bayes | 0.9440 | 0.8689 | 0.9500 | 0.9076 |

Compared with Multinomial Naive Bayes on word counts, Complement Naive Bayes
increased accuracy from 94.20% to 94.40% and F1-score from 90.42% to 90.76%.
The improvement was modest, while precision remained almost unchanged.

### Text Output Files

- `text_model_comparison.csv`
- `text_model_comparison_all.csv`
- `complement_nb_confusion_matrix.csv`

## Important Dataset Limitation

The supplied `emails.csv` contains precomputed word-count features rather than
raw email text. Therefore, TF-IDF was created using TfidfTransformer on the
existing count matrix. Raw-text cleaning and direct application of
CountVectorizer or TfidfVectorizer could not be demonstrated with this file.

## Tools and Libraries

- Python
- pandas
- NumPy
- scikit-learn
- OpenCV / image-processing libraries used in Part A
- Jupyter Notebook

## Reproducibility

The experiments used stratified 80:20 train-test splits with random_state=42.
Evaluation included accuracy, precision, recall, F1-score, confusion matrices,
and timing measurements.

## Conclusion

The image experiments achieved 95.00% accuracy with Logistic Regression.
For email classification, word-count features with Multinomial Naive Bayes
achieved 94.20% accuracy, while Complement Naive Bayes achieved 94.40%.
TF-IDF yielded higher precision but lower recall and F1-score in this run.

Results are specific to the supplied datasets, selected features, models,
and train-test split.
"""

readme_path = os.path.join(submission_dir, "README.md")

with open(readme_path, "w", encoding="utf-8") as file:
    file.write(readme_content.strip() + "\n")

print("README created successfully:")
print(readme_path)
