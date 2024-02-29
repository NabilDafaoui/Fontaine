import librosa
import time

# Load the audio file
y, sr = librosa.load('musique.mp3.wav')

# Find the onset times
onset_times = librosa.onset.onset_detect(y=y, sr=sr, units='time')

# Find the beat times
tempo, beat_times = librosa.beat.beat_track(y=y, sr=sr, units='time')

print(beat_times)
print(onset_times)

print(len(onset_times))
print(len(beat_times))