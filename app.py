import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))


    return " ".join(y)

with open('model2.pkl', 'rb') as file:
    model = pickle.load(file)
with open('vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)


# tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
# model = pickle.load(open('model.pkl', 'rb'))

st.title("SMS Spam Classifier")

input_msg = st.text_area("Enter the message")

if st.button("Predict"):

    # 1. Preprocess the input
    transformed_msg = transform_text(input_msg)
    # 2. Transform the input using the TF-IDF vectorizer
    tfidf_input = tfidf.transform([transformed_msg])
    # 3. Predict the class using the model
    result = model.predict(tfidf_input)[0]
    # 4. Display the result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")