from scipy.signal import stft
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np

# Can't seem to get the data to properly read
data, samplerate = sf.read("Guitar.wav")
print(data)
# data = data.astype(np.float32)

f, t, Zxx = stft(data, fs=samplerate)

plt.pcolormesh(t, f, np.abs(Zxx))
plt.ylabel('Hz')
plt.xlabel('Sec')
plt.show()
