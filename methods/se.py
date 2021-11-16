from nltk import sent_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

from utils.language import recognize


def abstract(text: str):
    language = recognize(text)

    documents = sent_tokenize(text, language=language)
    vectorizer = TfidfVectorizer(stop_words=stopwords.words(language))

    tf_idf = vectorizer.fit_transform(documents)

    threshold = 0
    for i in range(tf_idf.shape[0]):
        doc_tfidf = [val for val in tf_idf[i, :].toarray()[0] if val != 0]
        threshold += sum(doc_tfidf) / len(doc_tfidf)
    threshold = tf_idf.shape[0] / threshold

    summary = []
    for i in range(tf_idf.shape[0]):
        doc_tfidf = [val for val in tf_idf[i, :].toarray()[0] if val != 0]
        avg = sum(doc_tfidf) / len(doc_tfidf)
        if avg >= threshold * 0.1:
            summary.append(documents[i])

    return summary
