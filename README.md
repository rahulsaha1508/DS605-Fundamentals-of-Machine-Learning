# Airbnb Price Prediction

## Project Overview

This project predicts the nightly price of Airbnb listings using machine learning.

The project uses the NYC Airbnb Open Data dataset. The target variable is the listing price per night.

## Objectives

- Analyze the Airbnb dataset.
- Handle missing values and invalid data.
- Detect and remove extreme price outliers.
- Perform feature engineering.
- Train and compare regression models.
- Tune the best-performing model.
- Deploy the final model using Streamlit.

## Dataset

Dataset: NYC Airbnb Open Data

Target variable:

- price

Important features:

- neighbourhood_group
- neighbourhood
- room_type
- latitude
- longitude
- minimum_nights
- number_of_reviews
- reviews_per_month
- calculated_host_listings_count
- availability_365

## Data Preparation

The following preprocessing steps were performed:

- Removed unnecessary columns.
- Handled missing values.
- Removed invalid prices.
- Removed duplicate rows.
- Detected and removed extreme price outliers.
- Created total_review_activity.
- Created host_type.
- Created availability_type.
- Applied median imputation to numerical features.
- Applied most-frequent imputation to categorical features.
- Applied standardization to numerical features.
- Applied one-hot encoding to categorical features.

## Models Used

The following regression models were trained:

1. Linear Regression
2. Random Forest Regressor
3. Tuned Random Forest Regressor

## Model Results

| Model | MAE | RMSE | R2 Score |
|---|---:|---:|---:|
| Linear Regression | 33.740816 | 46.010775 | 0.532476 |
| Random Forest | 31.285345 | 43.510707 | 0.581903 |
| Tuned Random Forest | 31.012165 | 43.106397 | 0.589637 |

## Final Model

The Tuned Random Forest model was selected because it achieved:

- Lowest MAE
- Lowest RMSE
- Highest R2 Score

Final model performance:

- MAE: 31.012165
- RMSE: 43.106397
- R2 Score: 0.589637

## Application

A Streamlit application was developed to allow users to enter Airbnb listing details and receive a predicted nightly price.

To run the application:

```bash
python -m streamlit run app.py