from Get_Tweets import get_tweets
from Preprocess_Tweets import preprocess_tweets
from Topic_process import topic_process
from cosine_similarity import cosine_similarity_script
from Preprocess_Emotions import preprocess_emotions_script
from threading import Thread
import os

preprocess_emotions_script()
while True:
    scelta = input("""
***********************************************************************
*                          TOPIC FILM ADVICE                          *
*                         CONSOLE DI GESTIONE                         *
*   Software di Andrea Di Benedetto, Angelo Megna, Maria Sciortino    *
*                               Anno 2019                             *
***********************************************************************
* (1) Download tweets                                 (Get_Tweets.py) *
* (2) Preprocessing dei tweet                  (Preprocess_Tweets.py) *
* (3) Estrazione dei topic dai tweet               (Topic_process.py) *
* (4) Calcolo similarità tweet - trame                                *
*     ed estrazione dell'emozione              (cosine_similarity.py) *
* (Q) Uscita                                                          *
*                                                                     *
* AVVISO: IL TASK (4) RICHIEDE L'ESECUZIONE DI TUTTI I TASK           *
*         PRECEDENTI ALMENO UNA VOLTA!!!                              *
***********************************************************************
READY > """).upper()

    if scelta == '1':
        pass
        t1 = Thread(target=get_tweets())
        t1.daemon = True
        t1.start()
    elif scelta == '2':
        t2 = Thread(target=preprocess_tweets())
        t2.daemon = True
        t2.start()
    elif scelta == '3':
        t3 = Thread(target=topic_process())
        t3.daemon = True
        t3.start()
    elif scelta == '4':
        t4 = Thread(target=cosine_similarity_script())
        t4.daemon = True
        t4.start()
    elif scelta == 'Q':
        print("FINE")
        os.remove("text_emotion_prepro.csv")
        exit(0)
