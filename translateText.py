"""modules"""
import threading
import time
import os
from  gtts import gTTS
from pygame import mixer
from googletrans import Translator


path = 'text.txt'
userDataFromTextFile = ""
destUserDataAfterTranslation = ''

def readUserData():

    """this function will read the data provided by the user"""
    global path, userDataFromTextFile
    while True:
        with open(path,'r') as readInformation :
            userDataFromTextFile = readInformation.read()



    pass
def translateTheData():


    global  destUserDataAfterTranslation
    trans = Translator()
    translated = trans.translate(text = f'{userDataFromTextFile}' ,src='en',dest="hi")
    destUserDataAfterTranslation = translated.text
    speakDataByUser(destUserDataAfterTranslation)






def speakDataByUser(datas):
    mixer.init()
    print(datas)
    speakLang = gTTS(text= f'{datas}',lang='hi',slow=True)
    speakLang.save('mylang.mp3')
    mixer.music.load('mylang.mp3')
    mixer.music.play()
    storeUserData()
    while True:
        x=input()
        mixer.music.stop()
        break




def storeUserData():

    with open('history.txt','a') as dataStore:
        dataStore.write(f'kaho')



t1 = threading.Thread(target=readUserData,daemon=True)
t2 = threading.Thread(target=translateTheData)
t1.start()
t2.start()
