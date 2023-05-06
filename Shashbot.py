from newspaper import Article
from googlesearch import search
import nltk


def setup():
    nltk.download("punkt", quiet=True)
    nltk.download("wordnet", quiet=True)


def answer_query(query):
    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
        article = Article(url)

    article.download()
    article.parse()
    article.nlp()
    result = article.text
    return result
