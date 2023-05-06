#Shashbot
program=True
while program==True:
    import streamlit as st
    from newspaper import Article
    import numpy as np
    import warnings
    import nltk
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    warnings.filterwarnings('ignore')
    nltk.download('punkt',quiet=True)
    nltk.download('wordnet',quiet=True)
    query=st.text_input("Hi there! I am Shashbot. How may I help you today?") 
    try:
       from googlesearch import search
    except ImportError:
       print("No module named 'google' found")
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
       article= Article(j)
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    print(corpus)
