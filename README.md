# 📊 Social Media Monitoring Dashboard using NLP

## 🚀 Project Overview

This project is a **Social Media Monitoring System** that analyzes textual data (posts, comments, etc.) using Natural Language Processing (NLP) techniques to extract meaningful insights such as sentiment and trends.

---

## 🧠 Features Implemented (Current Stage)

* ✅ Data Input using CSV dataset
* ✅ Text Preprocessing (Cleaning, Tokenization, Stopword Removal)
* 🔄 Sentiment Analysis (Next Stage)
* 🔄 Keyword Extraction
* 🔄 Visualization Dashboard

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NLTK**
* **Matplotlib (upcoming)**
* **WordCloud (upcoming)**
* **Flask (upcoming)**

---

## 📁 Project Structure

```
social-media/
│
├── backend/
│   ├── app.py
│   └── modules/
│       ├── preprocessing.py
│       ├── sentiment.py
│       └── keywords.py
│
├── data/
│   └── sample_data.csv
│
├── frontend/ (to be implemented)
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone git@github.com:Anugrah0619/social-media.git
cd social-media
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Download NLTK Resources

```bash
python
```

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
exit()
```

---

### 5. Run the Application

```bash
cd backend
python app.py
```

---

## 📊 Sample Output

* Cleaned text after preprocessing
* Ready for sentiment analysis

---

## 📌 Future Enhancements

* Sentiment Analysis using VADER
* Keyword Extraction
* Visualization (Charts + WordCloud)
* Web Dashboard (Flask / Streamlit)
* Live Data via API

---

## 👨‍💻 Contributors

* Anugrah Kulkarni
* Stavya Joshi
* Shreyas Sachan

---

## 📄 License

This project is for academic purposes.
