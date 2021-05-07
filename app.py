import streamlit as st
import sklearn
import joblib
model = joblib.load('/content/Sentiment_model')
st.title('Sentiment Analysis')
ip = st.text_input("Enter the Tweet")
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])  
