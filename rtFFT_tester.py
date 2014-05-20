__author__ = 'Ralph Leyva'

import pyaudio

from matplotlib import pyplot

import rt_FFT


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

test = pyplot
test.ion()

while 1:
    p = pyaudio.PyAudio()
    strm = p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)

    soundData = rt_FFT.soundRec(strm, 10)
    freqData = rt_FFT.freqGen(RATE, soundData)

    test.subplot(3, 1, 1)
    test.plot(soundData)

    test.subplot(3, 1, 2)
    test.plot(freqData.freq, freqData.fftr)

    test.subplot(3, 1, 3)
    test.plot(freqData.freq, freqData.fftb)

    test.draw()
    test.clf()
    strm.close()

