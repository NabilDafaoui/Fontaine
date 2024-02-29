import turtle
import librosa
import numpy as np
import time

# Charger le fichier audio
y, sr = librosa.load('musique.mp3')

# Extraire les basses en utilisant la transformée de Fourier
D = librosa.stft(y)
mag, phase = librosa.magphase(D)
bass = librosa.feature.spectral_centroid(S=mag, sr=sr)
bass_mean = bass.mean()

# Créer la fenêtre de dessin Turtle
wn = turtle.Screen()
wn.bgcolor("black")

# Créer le cercle initial
circle = turtle.Turtle()
circle.shape("circle")
circle.color("white")
circle.shapesize(1)
circle.penup()
circle.goto(0, 0)

# Fonction pour agrandir le cercle en fonction des basses
def update_circle(frame):
    # Calculer la taille du cercle en fonction du niveau des basses
    size = 1 + ((bass[frame] - bass_mean) / 100)
    # Obtenir la taille maximale du cercle
    max_size = np.max(size)
    # Mettre à jour la taille du cercle
    circle.shapesize(max_size)

# Effectuer l'animation en boucle
for i in range(len(bass[0])):
    print((bass[0][i] - bass_mean) / 100)
    # update_circle(i)
    time.sleep(1)
print("FIN")
turtle.done()