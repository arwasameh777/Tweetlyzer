import streamlit as st
import joblib

# Load the model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Tweet Sentiment Analysis")

user_input = st.text_area("Enter the tweet:")

if st.button("Analyze"):
    if user_input:
        text_tfidf = vectorizer.transform([user_input])
        prediction = model.predict(text_tfidf)[0]
        st.write("Prediction:", prediction)
