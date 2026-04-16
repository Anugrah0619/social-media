# 📊 Social Media Monitoring Dashboard using NLP

## 🚀 Project Overview

This project is a **Social Media Monitoring System** that analyzes textual data (posts, comments, etc.) using Natural Language Processing (NLP) techniques to extract insights such as sentiment and trending keywords.

The system processes unstructured text data and converts it into meaningful visual insights through an interactive dashboard.

---

## 🧠 Features

* ✅ Data Input using CSV dataset
* ✅ Text Preprocessing (Cleaning, Tokenization, Stopword Removal)
* ✅ Sentiment Analysis using VADER
* ✅ Keyword Extraction using Frequency Analysis
* ✅ Data Visualization (Charts + Word Cloud)
* ✅ Interactive Dashboard using Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NLTK**
* **VADER Sentiment Analyzer**
* **Matplotlib**
* **WordCloud**
* **Streamlit**
* **Git & GitHub**

---

## 📁 Project Structure

```
social-media/
│
├── backend/
│   └── modules/
│       ├── preprocessing.py
│       ├── sentiment.py
│       ├── keywords.py
│       └── visualization.py
│
├── data/
│   └── sample_data.csv
│
├── outputs/
│   ├── sentiment.png
│   ├── keywords.png
│   └── wordcloud.png
│
├── app_streamlit.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone git@github.com:Anugrah0619/social-media.git
cd social-media
```

---

### 2️⃣ Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Download NLTK Data

```
python
```

```
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
exit()
```

---

## ▶️ Run Backend (Optional)

```
cd backend
python app.py
```

---

## 💻 Run Dashboard (Main)

```
streamlit run app_streamlit.py
```

👉 Open in browser:
http://localhost:8501

---

## 📊 Output

The system provides:

* Cleaned text data
* Sentiment classification (Positive/Negative/Neutral)
* Sentiment distribution charts
* Top keywords
* Word cloud visualization

---

## 📌 Future Enhancements

* Real-time data collection using Twitter API
* Advanced keyword extraction using TF-IDF
* Database integration (MongoDB)
* Deployment on cloud platforms

---

## 👨‍💻 Contributors

* Anugrah Kulkarni
* Stavya Joshi
* Shreyas Sachan

---

## 📄 License

This project is developed for academic purposes.
