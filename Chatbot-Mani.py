# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:24:35 2020

@author: manid
"""


import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
f = open('rs.txt','r',errors='ignore')
raw = f.read()

raw = raw.lower()

nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)


lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return[lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
    
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey","how are you","Namaskaram")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me","Namaskaram"]

def greeting(sentence):
    
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    
    TfidVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words='english')
    tfidf = TfidVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"Sorry, I don't understand you, can you try once more"
        
        return robo_response
    else:
        robo_response=robo_response+sent_tokens[idx]
        return robo_response

flag = True

print("Mani: My name is Mani. I am a interactive bot which will answer your queries about Rohit Sharma!! If you want to exit type Bye!")


while(flag==True):
    user_response = input()
    user_response = user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' or user_response=='thanks a lot' or user_response=='danyawad'):
            flag == False
            print("you are most welcome. . .")
        else:
            if(greeting(user_response)!=None):
                print("Mani:" +greeting(user_response))
            else:
                print("Mani:", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        
        flag = False
        print("Mani: Bye! take care come back later!!")
        

        
    
    
