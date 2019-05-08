# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:30:13 2019

@author: Carol
"""

#https://towardsdatascience.com/build-your-first-chatbot-using-python-nltk-5d07b027e727

from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"meu nome é (.*)",
        ["Olá %1, Como você está hoje ?",]
    ],
     [
        r"qual o seu nome ?",
        ["Meu nome é Chatty e eu sou um chatbot!",]
    ],
    [
        r"como voc(.*) est(.*)?",
        ["Estou bem\nE você?",]
    ],
    [
        r"tudo bem",
        ["Estou bem\nE você?",]
    ],
    [
        r"desculpe(.*)",
        ["Está tudo bem","OK, deixa para lá!",]
    ],
    [
        r"eu (.*) bem",
        ["Bom ouvir isso","Tudo bem :)",]
    ],
    [
        r"oi|olá|eae",
        ["Olá", "Oii","Eaewww, blz?"]
    ],
    [
        r"(.*) idade?",
        ["Eu sou um programa de computador rsrs\nSério você está me perguntando isso?",]
        
    ],
    [
        r"(.*) criou ?",
        ["Fui criado em Python com ajuda da biblioteca NLTK ","top secret ;)",]
    ],
    [
        r"(.*) (cidade|localização) ?",
        ['São Paulo, na Faria Lima',]
    ],
    [
        r"(.*)preço(.*)dolar(.*)?",
        ["Agora está 3.80","Você pode verificar no site","Alto demais!"]
    ],
    [
        r"como (.*) saúde(.*)",
        ["Eu sou um programa de computador, então estou sempre saudável rsrs ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
],
    [
        r"quit",
        ["Se cuida. Te vejo em breve :) ","Foi legal conversar com você. Te vejo em breve :)"]
],
]
def chatty():
    print("Olá, Eu sou Chatty e eu falo bastante ;)\nPor favor escreva em minusculo. Escreva quit para sair ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    chatty()