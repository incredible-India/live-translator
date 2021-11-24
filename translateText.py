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

    with open(path,'r') as readInformation :
        userDataFromTextFile = readInformation.read()





    pass
def translateTheData():


    global  destUserDataAfterTranslation
    trans = Translator()
    translated = trans.translate(text = f'{userDataFromTextFile}' ,src='en',dest="kn")
    destUserDataAfterTranslation = translated.text
    speakDataByUser(destUserDataAfterTranslation)

def speakDataByUser(datas):
    mixer.init()
    print(userDataFromTextFile,'\n',datas)

    speakLang = gTTS(text= f'{datas}',lang='kn',slow=True)
    speakLang.save('mylang.mp3')
    mixer.music.load('mylang.mp3')
    mixer.music.play()
    storeUserData()
    time.sleep(3)
    mixer.music.stop()





def storeUserData():

    with open('history.txt','a' ,encoding='utf-8') as dataStored:
        dataStored.write(f'\n{userDataFromTextFile} >>  translated to >> \t {destUserDataAfterTranslation}\n')


t1 = threading.Thread(target=readUserData,daemon=True)
t2 = threading.Thread(target=translateTheData)
t1.start()
t2.start()
