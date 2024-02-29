import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import datetime
import IPython
import turtle
import pygame
import time

def echelonner_tableau(tableau):
    min_val = min(tableau)
    max_val = max(tableau)
    echelonne = []
    for val in tableau:
        echelonne.append((val - min_val) / (max_val - min_val) * 100)
    return echelonne

window = turtle.Screen()
window.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")
t.hideturtle()
t.speed(0)

path = 'musique2.mp3'

y, sr = librosa.load(path,sr=None)

IPython.display.Audio(y,rate=sr)

i=0
# while(i<len(y)):
#     if(i%22105!=0 or y[i]<0):
#         y[i]=0
#     i+=1

print(len(y))

fig, ax = plt.subplots()
librosa.display.waveshow(y,sr=sr,ax=ax)

y=echelonner_tableau(y)

pygame.init()
pygame.mixer.music.load(path)
pygame.mixer.music.play(-1)

frame_time = (3*60+3)/len(y)
print(frame_time)

max_amplitude = max(y)

for i in range(0,len(y),22105):
    if(y[i]!=0):
        t.color("#000000")
        t.begin_fill()
        print((y[i]))
        t.circle((y[i]))
        t.end_fill()
        time.sleep(0.5)
        t.clear()