% Load audio file
[y, Fs] = audioread('/home/rgukt/Downloads/Chorus.wav');

% Reverse the audio signal
reversed_audio_data = flipud(y);

% Save the reversed audio to a new file
audiowrite('reversed_audio.wav', reversed_audio_data, Fs);
