import numpy as np
import soundfile as sf

# Load audio file
audio_data, sample_rate = sf.read('/home/rgukt/Downloads/Jazz.wav')

# Reverse the audio signal
reversed_audio_data = np.flip(audio_data)

# Save the reversed audio to a new file
sf.write('reversed_audio.wav', reversed_audio_data, sample_rate)

