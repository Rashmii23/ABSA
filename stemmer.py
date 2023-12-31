# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QPPh-5Kf_CIwTb9DiUrVJ0BQAgNU3XSC

#Preprocessing dataset
Stemming the news healdine using snowball stemmer
"""

import pandas as pd
from snowballstemmer import stemmer

nepali_stemmer = stemmer("nepali")

def stem_sentence(sentence):
    words = sentence.split()
    stemmed_words = []
    for word in words:
        stemmed_word = nepali_stemmer.stemWord(word)
        stemmed_words.append(stemmed_word)
    stemmed_sentence = " ".join(stemmed_words)
    return stemmed_sentence

# Read the data from the CSV file
df = pd.read_csv("input1.csv")

# Apply stemming to the 'Text' column and create a new column 'Text_Stemmed'
df['Text_Stemmed'] = df['Text'].apply(stem_sentence)

# Save only the 'Text_Stemmed' and 'Term' columns to a new CSV file named "output.csv"
df[['Text_Stemmed', 'Term']].to_csv("input_final.csv", index=False)

print(df[['Text_Stemmed', 'Term']])

"""Costumizing snowball stemmer for nepali dataset"""

from nepalitokenizers import WordPiece
import snowballstemmer

class CustomNepaliTokenizer:

    def __init__(self):
        self.stemmer = snowballstemmer.NepaliStemmer()
        self.wordpiece_tokenizer = WordPiece()

    def tokenize_and_stem(self, text):
        # Remove punctuations and split text into words
        punctuations = ['।', ',', ';', '?', '!', '—', '-', '.', '’', '‘']
        for punctuation in punctuations:
            text = text.replace(punctuation, ' ')
        words = text.strip().split()

        # Stem each word and collect the stemmed tokens
        stemmed_tokens = [self.stemmer.stemWord(word) for word in words]

        return stemmed_tokens

    def tokenize_to_ids(self, text):
        tokens = self.wordpiece_tokenizer.encode(text)
        return tokens.ids

    def decode(self, ids):
        return self.wordpiece_tokenizer.decode(ids)

# Example usage:
if __name__ == "__main__":
    tokenizer1= CustomNepaliTokenizer()
    text = "गुडविल फाइनान्सले यस वर्ष लाभांश नदिने"
    tokens = tokenizer1.tokenize_and_stem(text)
    print(tokens)