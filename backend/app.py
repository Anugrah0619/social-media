import pandas as pd
from modules.preprocessing import clean_text

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

if __name__ == "__main__":
    print("👉 Inside main block")
    
    df = load_data()
    
    if df is not None:
        df = preprocess_data(df)