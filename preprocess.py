from nltk.corpus import stopwords
import re
import nltk
import string
from nltk.tokenize import word_tokenize
import spacy

#nltk.download('punkt')
#nltk.download('stopwords')
nltk.data.path.append('models//nltk_data')

class Preprocess:

    def __init__(self) -> None:
        self.stop_words = stopwords.words('german')
        self.nlp = spacy.load('models//de_core_news_sm-3.1.0') #models//de_core_news_sm-3.1.0 #de_core_news_sm

    def clean_text(self, text, embedding=False):
        ''''Text cleaning for prediction'''
        #Removing all single chracters
        text = re.sub(r'\b\w\b', " ", text, flags=re.I)
        #removing all numbers and alhpanumeric combinations
        text = re.sub(r"\S*\d\S*", " ", text, flags=re.I)
        if not embedding:
            #Removing all punctations and keeping for word embeddings
            text = text.translate(str.maketrans("", "", string.punctuation)) 
        #removing extra spaces 
        text = re.sub('\s+', " ", text, flags=re.I).strip() 
        word_tokens = word_tokenize(text)
        #words_tokens_lower = [word.lower() for word in word_tokens]
        text = text.lower()
        if embedding:
            # no stemming, lowering and punctuation / stop words removal
            words_filtered = word_tokens
        else:
            #words_filtered = [stemmer.stem(word) for word in words_tokens_lower if word not in stop_words]
            text = ' '.join(word for word in text.split() if word not in self.stop_words)
            words_filtered = [x.lemma_ for x in self.nlp(text)]
        text_clean = " ".join(words_filtered)
        return text_clean