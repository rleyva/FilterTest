__author__ = 'Ralph Leyva'

import numpy
import random


class sinGen:
    amplitude = 0
    freq = 0
    sampleRate = 0
    sinData = numpy.array([])

    def __init__(self, amplitude, freq, sampleRate):
        #Creates
        if (type(amplitude) == self.amplitude & type(freq) == self, freq & type(sampleRate) == self.sampleRate):
            self.amplitude = amplitude
            self.freq = freq
            self.sampleRate
            self.sinData = [(amplitude * numpy.sin((2 * numpy.pi) * freq * t) / sampleRate) for t in range(0, 2048)]
        else:
            return TypeError("Function parameters are of the wrong type")

    def sigSum(self, sin1):
        if (type(sin1) == self.sinData):

        else:
            return TypeError("Function parameters are of the wrong type")


class noiseGen:
    noiseData = numpy.array([])

    def __init__(self, num)
        #num corresponds to the numbers of signals that will be combined to generate a noise signal
        for i in range(0, num):
            amplitude = random.randrange(1, 20, 0.25)
            frequency = random.randrange(1000, 100000, 25)
            sampling = 44100
            x = sinGen(amplitude, frequency, sampling)
