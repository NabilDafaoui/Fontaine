import turtle
import time
import random
import librosa
import numpy as np
import pygame
import matplotlib.pyplot as plt

def palette_couleur(nombre_couleurs):
    """Create a palette of RGB colors ranging from warm to cool."""
    palette = []
    for i in range(nombre_couleurs):
        r, g, b = 0, 0, 0
        if i < nombre_couleurs / 2:
            r = int(255 * (i / (nombre_couleurs / 2)))
            g = 0
            b = 255 - r
        else:
            r = 255 - int(255 * ((i - nombre_couleurs / 2) / (nombre_couleurs / 2)))
            g = int(255 * ((i - nombre_couleurs / 2) / (nombre_couleurs / 2)))
            b = 0
        palette.append((r, g, b))
    return palette

def rgb_to_hex(rgb):
    if len(rgb) != 3:
        raise ValueError("Le triplet RGB doit contenir 3 valeurs")
    if any(c < 0 or c > 255 for c in rgb):
        raise ValueError("Les valeurs du triplet RGB doivent être comprises entre 0 et 255")

    hex_code = "#{:02x}{:02x}{:02x}".format(*rgb)
    return hex_code

window = turtle.Screen()
window.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

audio_file = 'musique2.mp3'
y, sr = librosa.load(audio_file)

n_fft = 2048
hop_length = 512
frame_time = (3*60+3)/519

pitch_list = []
for i in range(0, len(y)-n_fft, hop_length):
    frame = y[i:i+n_fft]
    pitch, _ = librosa.piptrack(y=frame, sr=sr)
    if pitch.any():
        pitch_mean = librosa.pitch_tuning(pitch[pitch > 0])
        pitch_mean = int((pitch_mean+1)*5)
        pitch_list.append(pitch_mean)

color = palette_couleur(10)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr, hop_length=1024, start_bpm=240)
tempo_frames = librosa.tempo_frequencies(len(beat_frames)-1, hop_length=1024, sr=sr)

tab = [tempo_frames[i] for i in range(len(tempo_frames))]
tab[0] = 0

print(len(beat_frames))
print(color)

max_tempo = max(tab)
coef = 10/max_tempo

tab_echelle = [tab[i]*coef for i in range(len(tab))]

print(tab_echelle)

volume = np.abs(librosa.stft(y))

volume_int = volume.astype(int)

print(volume)

pygame.init()
pygame.mixer.music.load("musique.mp3")
pygame.mixer.music.play(-1)
for i in range(len(y)):
    if(y[i]!=0)
        t.color(rgb_to_hex("#FFFFF"))
        t.begin_fill()
        t.circle(y[i]*100)
        t.end_fill()
        time.sleep(1)
        t.clear()