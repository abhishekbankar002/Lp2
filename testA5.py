import nltk
from nltk.chat.util import reflections, Chat

pair = [
	['Hi|Hello|sup|Hola|Holla', ['Hello', 'Hi', 'Hey there']],
	['(.*) doing?', ['...Creating Robot Army', 'Chilling']],
	['(.*) actor|moviestar', ['Robert Downey Jr']],
	['(.*) created you?', ['Abhishek created me!!']],
	['quit', ['Bye! See you soon','Adios Amigos']]
]


def chat():
	print('Hi I am a chatbot created by Abhishek')
	chat = Chat(pair, reflections)
	chat.converse()


chat()
