# 📧 SMS & Email Spam Classifier

A machine learning project to classify SMS and email messages as **spam** or **not spam** using natural language processing and classification algorithms. This end-to-end project involves data preprocessing, EDA, model building, and deployment with Streamlit — hosted on an AWS EC2 instance.

---

## 🚀 Project Highlights

- 🧼 **Data Cleaning** with `pandas`
- 📊 **Exploratory Data Analysis (EDA)** to uncover patterns
- 🧠 **Text Preprocessing** using `nltk` (tokenization, stemming, stopword removal)
- 🤖 **Model Building** with ML algorithms like Naive Bayes, SVM, and Logistic Regression
- 🎯 **Hyperparameter Tuning** for improved accuracy
- 🌐 **Interactive UI** built with **Streamlit**
- ☁️ **Deployed on AWS EC2** for real-time classification

## 🧰 Tech Stack

- **Python 3**
- **Pandas** for data handling
- **Matplotlib / Seaborn** for visualization
- **NLTK** for text processing
- **Scikit-learn** for machine learning
- **Streamlit** for interactive web app
- **AWS EC2** for deployment


## 🔍 Project Workflow

### 1. Data Cleaning
- Removed duplicates and null values
- Standardized column formats using `pandas`

### 2. Exploratory Data Analysis (EDA)
- Visualized class imbalance
- Analyzed word frequencies in spam vs. ham messages

### 3. Text Preprocessing
- Lowercasing, tokenization
- Stopword removal, stemming using **NLTK**

### 4. Model Building
- Used models like **Multinomial Naive Bayes**
- Applied **TF-IDF Vectorization**
- Performed fine-tuning for optimal accuracy

### 5. Deployment
- Built a web app using **Streamlit**
- Simple and clean user interface

### 6. Hosting
- Deployed the app on **AWS EC2**, making it accessible online

---

## 📦 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/Spandan752/Email-SMS-Spam-Classifier.git
   cd Email-SMS-Spam-Classifier

2. **Create virtual environment and activate it**
-- python -m venv venv
--  .\venv\Scripts\activate   # On Windows
-- source venv/bin/activate # On Linux/Mac

3. **Install dependencies**
-- pip install -r requirements.txt

4. **Run the Streamlit app**
-- streamlit run app.py
