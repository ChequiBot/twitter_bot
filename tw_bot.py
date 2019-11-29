
import tweepy
import random
import os
import time
import codecs

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_KEY = os.getenv('ACCESS_KEY')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET) 
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET) 
api = tweepy.API(auth)
           
#Minutos * Segundos * (Cuantas veces se repite = horas de intervalo)
#INTERVALO = 60 * 60 * 6 #Twittea cada 6 horas.
INTERVALO = 300
while True:
           
 with codecs.open('frases.txt', encoding='utf-8', errors='ignore') as myfile:
    frases = myfile.readlines()
           
 #Se genera un numero random el cual es utilizado como indice
 r = random.randint(0, 24)
 tweet = "@CamiMontielH " + frases[r]

 #Twitteamos
 try:
     if api.update_status(tweet):
         print("Twitteado")
 #Manejo de excepciones 
 except tweepy.error.TweepError as e:
     print(e)

 time.sleep(INTERVALO)
