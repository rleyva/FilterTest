__author__ = 'ralph'

import numpy
from matplotlib import pyplot as pp
import scipy

from noiseGen import shaper


freq = 20000
framerate = 44100
mySampleData = [numpy.cos(numpy.pi * a / framerate) for a in range(0, 1024)]
twentykHz_wave = [numpy.cos((2 * numpy.pi) * freq * a / framerate) for a in range(0, 1024)]

x = shaper(sampleData=mySampleData)

for i in range(0, 10):
    data = []
    for i in range(0, 1024):
        data.append(x.getNoise())

pp.subplot(4, 1, 1)
pp.plot(data)
pp.title("Generated Noise")

pp.subplot(4, 1, 2)
pp.plot(abs(scipy.fft(data)))
pp.title("Generated Noise Spectrum")

pp.subplot(4, 1, 3)
pp.plot(twentykHz_wave)
pp.title("20kHz Sine Wave")

pp.subplot(4, 1, 4)
pp.plot(abs(scipy.fft(twentykHz_wave)))
pp.title("Generated FFT for 20kHz Wave")

pp.show()