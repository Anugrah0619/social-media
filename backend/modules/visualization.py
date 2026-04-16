import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

# Create outputs folder if not exists
os.makedirs("../outputs", exist_ok=True)

def plot_sentiment_distribution(df):
    sentiment_counts = df["sentiment"].value_counts()

    plt.figure(figsize=(6, 6))
    sentiment_counts.plot.pie(
        autopct='%1.1f%%',
        colors=['green', 'red', 'blue']
    )
    plt.title("Sentiment Distribution")
    plt.ylabel("")
    
    plt.savefig("../outputs/sentiment.png")
    plt.show()


def plot_keyword_bar(keywords):
    words = [word for word, freq in keywords]
    freqs = [freq for word, freq in keywords]

    plt.figure(figsize=(8, 5))
    plt.bar(words, freqs)
    plt.title("Top Keywords")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=30)

    plt.savefig("../outputs/keywords.png")
    plt.show()


def generate_wordcloud(df):
    text = " ".join(df["clean_text"])

    wordcloud = WordCloud(width=800, height=400, background_color='black').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title("Word Cloud")

    plt.savefig("../outputs/wordcloud.png")
    plt.show()