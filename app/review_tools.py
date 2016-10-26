import pandas as pd
from textblob import TextBlob
import re

def preprocess_review(blob):
    return blob.lower().correct()

def stars_prior(score):
    """convert the review score (stars)
    to a sentiment score between -1 and 1
    min(score) = 1
    max(score) = 5
    """
    assert score <= 5
    assert score >= 1
    return (score-3)/2

def get_nouns(blob):
    lst = []
    for word,tag in blob.tags:
        if tag in ['NN','NNS','NNP','NNPS']:
            word = word.singularize().lemmatize()
            word = re.sub('[^a-zA-Z0-9]','',word)
            if word == '': continue
            lst.append(word)
    return lst

def extract_nouns(row,alpha=0.2):
    """Input is a row of the review dataframe"""
    text = row['text']
    sentiment = stars_prior(row['stars'])
    threshold = -alpha*sentiment
    #TODO use review sentiment as prior
    # for sentence sentiment
    blob = preprocess_review(TextBlob(text))
    words = {'positive':{},'negative':{}}
    for sentence in blob.sentences:
        sentiment = ['negative','positive'][int(sentence.polarity>threshold)]
        nouns = get_nouns(sentence) 
        for noun in nouns:
            words[sentiment][noun] = words[sentiment].get(noun,0)+1
    return words

def noun_count(revs):
    """revs is reviews for a particular business"""
    word_count = {'positive':{}, 'negative':{}}
    for i,rev in revs.iterrows():
        nouns = extract_nouns(rev)
        for sentiment, counts in nouns.items():
            for word,count in counts.items():
                word_count[sentiment][word] = word_count[sentiment].get(word,0)+count
    return word_count
