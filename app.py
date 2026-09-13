import streamlit as st
import pandas as pd
import joblib

model = joblib.load("airbnb_price_model.pkl")
preprocessor = joblib.load("airbnb_preprocessor.pkl")

st.set_page_config(
    page_title="Airbnb Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Airbnb Nightly Price Predictor")

st.write(
    "Enter the details of an Airbnb listing to predict its nightly price."
)

neighbourhood_group = st.selectbox(
    "Neighbourhood Group",
    [
        "Bronx",
        "Brooklyn",
        "Manhattan",
        "Queens",
        "Staten Island"
    ]
)

neighbourhood = st.text_input(
    "Neighbourhood",
    value="Midtown"
)

room_type = st.selectbox(
    "Room Type",
    [
        "Entire home/apt",
        "Private room",
        "Shared room"
    ]
)

latitude = st.number_input(
    "Latitude",
    value=40.7306,
    format="%.6f"
)

longitude = st.number_input(
    "Longitude",
    value=-73.9352,
    format="%.6f"
)

minimum_nights = st.number_input(
    "Minimum Nights",
    min_value=1,
    value=1,
    step=1
)

number_of_reviews = st.number_input(
    "Number of Reviews",
    min_value=0,
    value=10,
    step=1
)

reviews_per_month = st.number_input(
    "Reviews per Month",
    min_value=0.0,
    value=1.0,
    step=0.1
)

calculated_host_listings_count = st.number_input(
    "Host Listing Count",
    min_value=1,
    value=1,
    step=1
)

availability_365 = st.number_input(
    "Availability in 365 Days",
    min_value=0,
    max_value=365,
    value=180,
    step=1
)

total_review_activity = (
    number_of_reviews * reviews_per_month
)

if calculated_host_listings_count <= 1:
    host_type = "Single Listing"
elif calculated_host_listings_count <= 5:
    host_type = "Small Host"
elif calculated_host_listings_count <= 20:
    host_type = "Medium Host"
else:
    host_type = "Large Host"

if availability_365 <= 30:
    availability_type = "Low Availability"
elif availability_365 <= 180:
    availability_type = "Medium Availability"
else:
    availability_type = "High Availability"

input_data = pd.DataFrame({
    "neighbourhood_group": [neighbourhood_group],
    "neighbourhood": [neighbourhood],
    "latitude": [latitude],
    "longitude": [longitude],
    "room_type": [room_type],
    "minimum_nights": [minimum_nights],
    "number_of_reviews": [number_of_reviews],
    "reviews_per_month": [reviews_per_month],
    "calculated_host_listings_count": [
        calculated_host_listings_count
    ],
    "availability_365": [availability_365],
    "total_review_activity": [total_review_activity],
    "host_type": [host_type],
    "availability_type": [availability_type]
})

if st.button("Predict Price"):

    processed_input = preprocessor.transform(
        input_data
    )

    prediction = model.predict(
        processed_input
    )

    predicted_price = prediction[0]

    st.success(
        f"Predicted nightly price: ${predicted_price:.2f}"
    )