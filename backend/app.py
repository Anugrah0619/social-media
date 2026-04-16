import pandas as pd
from modules.preprocessing import clean_text
from modules.sentiment import get_sentiment
from modules.keywords import extract_keywords

print("🚀 File is running...")

def load_data():
    try:
        df = pd.read_csv("../data/sample_data.csv")
        print("✅ Data Loaded Successfully")
        return df
    except Exception as e:
        print("❌ Error loading data:", e)
        return None

def preprocess_data(df):
    df["clean_text"] = df["text"].apply(clean_text)
    
    print("\n🧹 Cleaned Data:")
    print(df[["text", "clean_text"]])
    
    return df

def analyze_sentiment(df):
    df["sentiment"] = df["clean_text"].apply(get_sentiment)
    
    print("\n😊 Sentiment Analysis:")
    print(df[["clean_text", "sentiment"]])
    
    return df

def extract_top_keywords(df):
    keywords = extract_keywords(df["clean_text"].tolist())
    
    print("\n🔑 Top Keywords:")
    for word, freq in keywords:
        print(f"{word}: {freq}")
    
    return keywords

if __name__ == "__main__":
    print("👉 Inside main block")
    
    df = load_data()
    
    if df is not None:
        df = preprocess_data(df)
        df = analyze_sentiment(df)
        keywords = extract_top_keywords(df)