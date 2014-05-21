__author__ = 'Ralph Leyva'

import pyaudio
import time
from spectrum import *
import rt_FFT
from matplotlib import pyplot


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# p = pyaudio.PyAudio()
# strm = p.open(format=FORMAT,
#               channels=CHANNELS,
#               rate=RATE,
#               input=True,
#               frames_per_buffer=CHUNK)

# soundData = rt_FFT.soundRec(strm, 500)
# freqData = rt_FFT.freqGen(RATE, soundData)
# rt_FFT.freqPlot(soundData, RATE, freqData.freq, freqData.fftr, freqData.ffti, freqData.fftb)
#
# test = pyplot.plot(freqData.freq, freqData.fftb)
# pyplot.show()

# test = pyplot
# test.ion()

# This code currently works bt consumes way too mabny resources,
# and is really, really, REALLY slow!!! Perhaps using the animation
# libraries will fix this?

# THIS IS TRASH
# p = pyaudio.PyAudio()
# strm = p.open(format=FORMAT,
#               channels=CHANNELS,
#               rate=RATE,
#               input=True,
#               frames_per_buffer=CHUNK)
#
# while 1:
#     tStart = time.time()
#     p = pyaudio.PyAudio()
#     strm = p.open(format=FORMAT,
#                   channels=CHANNELS,
#                   rate=RATE,
#                   input=True,
#                   frames_per_buffer=CHUNK)
#     soundData = rt_FFT.soundRec(strm, 1)
#     freqData = rt_FFT.freqGen(RATE, soundData)
#
#     test.subplot(3, 1, 1)
#     test.plot(soundData)
#
#     test.subplot(3, 1, 2)
#     test.plot(freqData.freq, freqData.fftr)
#
#     test.subplot(3, 1, 3)
#     test.plot(freqData.freq, freqData.fftb)
#
#     test.draw(),
#     print 'Time: ', time.time() - tStart, ' seconds'
#     print 'Length of Data: ', len(freqData)
#     test.clf()
#     strm.close()
# #
# import matplotlib.pyplot as plt
# import numpy
#
# hl, = plt.plot([], [])
#
#
