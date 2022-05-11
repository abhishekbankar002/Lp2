# import nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# import warnings
# warnings.filterwarnings("ignore")
# import random
# import string
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
#
# f = open('chatbot.txt','r',errors = 'ignore')
# raw = f.read()
# raw = raw.lower()
# sent_tokens = nltk.sent_tokenize(raw)
# word_tokens = nltk.word_tokenize(raw)
#
#
# lemmer = nltk.stem.WordNetLemmatizer()
#
#
# def LemTokens(tokens):
#     return [lemmer.lemmatize(token) for token in tokens]
#
#
# remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
#
#
# def LemNormalize(text):
#     return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
#
#
# def response(user_response):
#     robo_response=''
#     sent_tokens.append(user_response)
#     TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
#     tfidf = TfidfVec.fit_transform(sent_tokens)
#     vals = cosine_similarity(tfidf[-1], tfidf)
#     idx = vals.argsort()[0][-2]
#     flat = vals.flatten()
#     flat.sort()
#     req_tfidf = flat[-2]
#     if(req_tfidf==0):
#         robo_response=robo_response+"I am sorry! I don't understand you"
#         return robo_response
#     else:
#         robo_response = robo_response+sent_tokens[idx]
#         return robo_response
#
#
# flag=True
# print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
#
#
# GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up","hey",]
# GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
#
#
# def greeting(sentence):
#     for word in sentence.split():
#         if word.lower() in GREETING_INPUTS:
#             return random.choice(GREETING_RESPONSES)
#
#
# while(flag==True):
#     user_response = input()
#     user_response=user_response.lower()
#     if(user_response!='bye'):
#         if(user_response=='thanks' or user_response=='thank you' ):
#             flag = False
#             print("ROBO: You are welcome..")
#         else:
#             if(greeting(user_response)!=None):
#                 print("ROBO: "+greeting(user_response))
#             else:
#                 print("ROBO: ",end="")
#                 print(response(user_response))
#                 sent_tokens.remove(user_response)
#     else:
#         flag=False
# print("ROBO: Bye! take care..")

import nltk
from nltk.chat.util import Chat, reflections

# print(reflections)

pairs = [
    ['my name is (.*)', ['Hello !']],
    ['(hi|hello|hey|holla|hola)', ['Hey there !', 'Hi there !', 'Hey !']],
    ['(.*) your name ?', ['My name is chitty']],
    ['(.*) doing ?', ['Making robo army !']],
    ['(.*) created you ?', ['‐‐‐ nobody created me i am the creator']],
    ['quit', ['Bye! See you soon', 'Adios Amigos']]
]

def chat():
    print("Hi! I am a chatbot created by Abhishek for your service")
    chat = Chat(pairs, reflections)
    chat.converse()


chat()