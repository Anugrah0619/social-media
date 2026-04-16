import pandas as pd

print("🚀 File is running...")

def load_data():
    try:
        df = pd.read_csv("../data/sample_data.csv")
        print("✅ Data Loaded Successfully")
        print(df.head())
        print("Total rows:", len(df))
        return df
    except Exception as e:
        print("❌ Error loading data:", e)
        return None

if __name__ == "__main__":
    print("👉 Inside main block")
    df = load_data()