import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load audio file
audio_data, sample_rate = librosa.load('/home/rgukt/Downloads/Chorus.wav')

# Plot audio signal
plt.figure(figsize=(10, 4))
librosa.display.waveshow(audio_data, sr=sample_rate)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal')
plt.show()

