__author__ = 'Ralph Leyva'

import pyaudio
from matplotlib import pyplot
import numpy
import rt_FFT

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
strm = p.open(format=FORMAT,
              channels=CHANNELS,
              rate=RATE,
              input=True,
              frames_per_buffer=CHUNK)

soundData = rt_FFT.soundRec(strm, 1)
freqData = rt_FFT.freqGen(RATE, soundData)
plt = pyplot
#rt_FFT.freqPlot(soundData, RATE, freqData.freq, freqData.fftr, freqData.ffti, freqData.fftb)
plt.plot(soundData)
while (1):
    soundData = rt_FFT.soundRec(strm, 1)
    rt_FFT.updateGraph(plt, soundData, len(soundData))