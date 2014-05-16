import pyaudio
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 0.1
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Recording...")
info = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    info.append(np.fromstring(stream.read(CHUNK), 'Int16'))

test = np.concatenate(info)

ax = plt.subplot(3, 1, 1)
plt.plot(test)
plt.title("Recorded Waveform")

plt.subplot(3, 1, 2)
left, right = np.split(abs(np.fft.fft(test)), 2)
plt.plot(abs(left))

plt.subplot(3, 1, 3)
plt.title("Waveform FFT")
leftFreq, rightFreq = np.split(np.fft.fftfreq(len(test), float(RECORD_SECONDS / RATE)), 2)
print rightFreq
plt.plot(rightFreq, left)
plt.show()
