#ACCURACY HMM

import os
import librosa
import numpy as np
from hmmlearn.hmm import GMMHMM
import pickle
import joblib
#from sklearn.externals import joblib
from python_speech_features import mfcc
import librosa.display
import matplotlib.pyplot as plt

import cv2
import pyaudio


def predict(voice,g):
    speakers =["nishant","padma","rajat","shreekar","shruthi"]
    #speakers =["nishant","padma","rajat"]

    threshold = 500
    l=2
    uppercutoff=20000
    lowercutoff=8000

    #open the test data and find its probability 
    #compare it with test probability and print predictions

    student = voice #SPEAKERS VOICE STORED



    file_path1="F:/voicerecog/"
    test_speech1 = student
    speech1, rate = librosa.core.load(file_path1+test_speech1)     #EXTRACT MFCC AND ADD IT OT FEATURE VECTOR
    feature_vectors12 = librosa.feature.mfcc(y=speech1, sr=rate)

    features1=feature_vectors12.transpose()
    print("No of Features ",np.shape(features1))

    #GET THE SCORE VALUES FOR EVERY MODEL CREATED FOR EACH SPEAKER
    x=[]

    path ="F:/voicerecog/models/"
    names = os.listdir(path)
    #print(names)

    h=[]
    for i in range(0,len(names)):
        m1=joblib.load("F:/voicerecog/models/"+str(names[i]) )
        p1 = m1.score(features1)
        p1=abs(p1)
        print("Score for Speaker ",i,"is ",p1)
        x.append(p1)

    y=x.index(min(x))
    #print(x)
    #print(x.index(min(x))+1)
    if min(x)<uppercutoff and min(x)>lowercutoff:
        g.append(speakers[y])
    else:
        print("cant recognise. Speak again")




labels=["N","N","N","N","N","R","R","R","R","R"]
g=[]
g1=[]
correct=0
wrong=0

voice="voicereg/voices"
v=os.listdir("F:/voicerecog/voices")

for i in range(0,len(v)):
    v1=voice+v[i]
    predict(v1,g)
#print(g)

for i in g:
    if i=="nishant":
        g1.append("N")
    elif i=="rajat":
        g1.append("R")

print(labels,g1)
i=0
while (i<len(g1)):
    if g1[i]==labels[i]:
        correct=correct+1
        i=i+1
    else:
        wrong=wrong+1
        i=i+1

print("predicted",correct,"correct out of 10")
    
