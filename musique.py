import librosa
import numpy as np

def palette_couleur(nombre_couleurs):
    """Create a palette of RGB colors ranging from warm to cool."""
    palette = []
    for i in range(nombre_couleurs):
        r, g, b = 0, 0, 0
        if i < nombre_couleurs / 2:  # warm colors
            r = int(255 * (i / (nombre_couleurs / 2)))
            g = 0
            b = 255 - r
        else:  # cool colors
            r = 255 - int(255 * ((i - nombre_couleurs / 2) / (nombre_couleurs / 2)))
            g = int(255 * ((i - nombre_couleurs / 2) / (nombre_couleurs / 2)))
            b = 0
        palette.append((r, g, b))
    return palette
    
#Charger le fichier audio
audio_file = 'musique.mp3'
y, sr = librosa.load(audio_file)

#Paramètres de la fenêtre d'analyse
n_fft = 2048
hop_length = 512

#Calculer la tonalité de chaque frame
pitch_list = []
for i in range(0, len(y)-n_fft, hop_length):
    frame = y[i:i+n_fft]
    pitch, _ = librosa.piptrack(y=frame, sr=sr)
    if pitch.any():
        pitch_mean = librosa.pitch_tuning(pitch[pitch > 0])
        pitch_list.append(pitch_mean)

# print(tonality_to_color([0,1]))

print(palette_couleur(5))