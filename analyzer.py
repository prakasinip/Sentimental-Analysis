!pip install nltk
!pip install numpy
!pip install pandas

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
nltk.download('punkt')

import pandas as pd
import numpy as np
import nltk
import io
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

with open('kindle.txt', encoding ='ISO-8859-2') as f:
	text = f.read()

sent_tokenizer = PunktSentenceTokenizer(text)
sents = sent_tokenizer.tokenize(text)

print(word_tokenize(text))
print(sent_tokenize(text))
