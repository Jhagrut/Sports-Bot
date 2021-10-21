"""
Cleaning Tools

Holds all functions for converting scraped twitter data into
the filtered.csv and clean.csv files.
"""

import pandas as pd
import os
from joblib import dump, load

# For further cleaning with word stemming and lemmatization:
import string
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Format the data from merged.csv to send to filtered.csv

def ifelse(boolean, ifValue, elseValue):
    if boolean:
        return ifValue
    else:
        return elseValue

def clean_text(txt):
    """""
    cleans the input text in the following steps
    1- replace contractions
    2- removing punctuation
    3- spliting into words
    4- removing stopwords
    5- removing leftover punctuations
    """""
    contraction_dict = {"ain't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not", "didn't": "did not",  "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not", "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",  "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would", "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would", "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam", "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have", "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock", "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have", "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is", "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as", "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would", "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have", "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have", "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are", "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",  "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is", "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have", "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have", "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have","you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have", "you're": "you are", "you've": "you have"}
    def _get_contractions(contraction_dict):
        contraction_re = re.compile('(%s)' % '|'.join(contraction_dict.keys()))
        return contraction_dict, contraction_re

    def replace_contractions(text):
        contractions, contractions_re = _get_contractions(contraction_dict)
        def replace(match):
            return contractions[match.group(0)]
        return contractions_re.sub(replace, text)

    # replace contractions
    txt = replace_contractions(txt)
   
    #remove punctuations
    txt  = "".join([char for char in txt if char not in string.punctuation])
    txt = re.sub('[0-9]+', '', txt)
   
    # split into words
    words = word_tokenize(txt)
   
    # remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
   
    # removing leftover punctuations
    words = [word for word in words if word.isalpha()]
   
    cleaned_text = ' '.join(words)
    return cleaned_text

def scrape_to_merge():
    fileList = [os.getcwd()  + '/TweetData/' + files 
                for files in os.listdir(os.getcwd()  + '/TweetData')]

    data = pd.read_csv('merged2.csv')
    
    for i in range(len(fileList)):
        data = data.append(pd.read_csv(fileList[i]))
        
    data = data.drop_duplicates()
    data.to_csv('merged2.csv', index=False)
    del data


def aggregate_merged(file, mergetype):
    if mergetype == 1:

        data = pd.read_csv(file)
        data['urls'] = data['urls'].apply(lambda x: str(x).lstrip("[").rstrip("]"))
        data['link_present'] = data['urls'].apply(lambda x: ifelse(len(x) > 0, 1, 0))
        data['photos'] = data['photos'].apply(lambda x: str(x).lstrip("[").rstrip("]"))
        data['photo_present'] = data['photos'].apply(lambda x: ifelse(len(x) > 0, 1, 0))
        data['retweet'] = data['retweet'].astype(bool).apply(lambda x: ifelse(x, 1, 0))

    else:

        data = pd.concat(file)

    final = data.groupby(['link', 'tweet']).agg({'replies_count': 'max', 'retweets_count': 'max', 'likes_count': 'max',
                                                 'link_present': 'max', 'photo_present': 'max', 'retweet': 'max'})

    final['replies_count'] = final['replies_count'].astype(int)
    final['retweets_count'] = final['retweets_count'].astype(int)
    final['likes_count'] = final['likes_count'].astype(int)
    final['link_present'] = final['link_present'].astype(int)
    final['photo_present'] = final['photo_present'].astype(int)
    final['retweet'] = final['retweet'].astype(int)

    final = final.reset_index(0).reset_index(0)

    return final

def append_labels(data, file):
    labeled = pd.read_csv(file)
    labeled = labeled[['injury_report', 'tweet']]
    labeled = labeled[labeled['injury_report'] != 'x']
    labeled = labeled.drop_duplicates()
    labeled = labeled.dropna()
    filtered = data.merge(labeled, on='tweet', how='left')
    try:
        filtered['injury_report'] = filtered['injury_report_y'].fillna('x')
        filtered.drop(['injury_report_x', 'injury_report_y'], axis=1, inplace=True)
    except KeyError:
        pass
    return filtered

def merged_to_filtered():
    file_aggregates = [aggregate_merged(filename, 1) for filename in os.listdir() if 'merged' in filename]
    filtered = aggregate_merged(file_aggregates, 0)
    filtered = append_labels(filtered, 'filtered2.csv')
    filtered.to_csv('filtered2.csv', index=False)

def label_filtered_duplicates():
    filtered = pd.read_csv('filtered2.csv')
    labeled_data = filtered[filtered['injury_report'] != 'x'][['tweet', 'injury_report']].drop_duplicates()
    labeled_data.to_csv('copy.csv', index=False)
    filtered = append_labels(filtered, 'copy.csv')
    filtered.to_csv('filtered2.csv', index=False)
    
def filtered_to_clean():
    data = pd.read_csv('filtered2.csv')
    data = data[data['injury_report'] != 'x']
    data = data[['injury_report', 'tweet']]
    data = data.drop_duplicates()
    data = data[data['tweet'].apply(lambda x: isinstance(x, str))]
    data['clean'] = data['tweet'].apply(lambda txt: clean_text(txt))
    data.dropna(inplace = True)
    data.to_csv('clean.csv', index=False)
    del data
    
def get_data_to_label():
    data = pd.read_csv('filtered2.csv')
    data = data[data['injury_report'] == 'x']
    data = data[['injury_report', 'tweet']]
    data.drop_duplicates(inplace = True)
    data.dropna(inplace = True)
    
    samples_to_label = data.sample(1000)
    samples_to_label.to_csv('sampled.csv')

    lgr = load('Classical Models//logistic_regression.joblib')
    v_tfidf = load('Classical Models//tfidf.joblib')

    data = data.sample(100000)
    data['clean'] = data['tweet'].apply(lambda txt: clean_text(txt))
    data['lgr_predictions'] = lgr.predict(v_tfidf.transform(data['clean']))
    positives = data[data['lgr_predictions'] == 1]
    positives = positives[['injury_report', 'tweet']]
    positives.to_csv('positive_samples.csv')
    del data

def label_new_data():
    filtered = pd.read_csv('filtered2.csv')
    filtered = append_labels(filtered, 'sampled.csv')
    filtered = append_labels(filtered, 'positive_samples.csv')
    filtered.to_csv('filtered2.csv', index=False)
    