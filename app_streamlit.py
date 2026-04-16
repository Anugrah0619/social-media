import streamlit as st
import pandas as pd
import sys

# Fix import path
sys.path.append("backend")

from modules.preprocessing import clean_text
from modules.sentiment import get_sentiment
from modules.keywords import extract_keywords

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Social Media Dashboard", layout="wide")

st.title("📊 Social Media Monitoring Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

# Load data
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/sample_data.csv")

# Validate column
if "text" not in df.columns:
    st.error("CSV must contain a 'text' column")
    st.stop()

# Raw data
st.subheader("📄 Raw Data")
st.dataframe(df)

# Preprocessing
df["clean_text"] = df["text"].apply(clean_text)

st.subheader("🧹 Cleaned Data")
st.dataframe(df[["text", "clean_text"]])

# Sentiment
df["sentiment"] = df["clean_text"].apply(get_sentiment)

st.subheader("😊 Sentiment Analysis")
st.dataframe(df[["clean_text", "sentiment"]])

# Sentiment chart
st.subheader("📊 Sentiment Distribution")
st.bar_chart(df["sentiment"].value_counts())

# Keywords
keywords = extract_keywords(df["clean_text"].tolist())

st.subheader("🔑 Top Keywords")
for word, freq in keywords:
    st.write(f"{word}: {freq}")

# Word Cloud
st.subheader("☁️ Word Cloud")

text = " ".join(df["clean_text"])

if text.strip():
    wordcloud = WordCloud(width=800, height=400, background_color='black').generate(text)

    fig, ax = plt.subplots()
    ax.imshow(wordcloud)
    ax.axis("off")

    st.pyplot(fig)
else:
    st.warning("No text available for word cloud")
