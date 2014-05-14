__author__ = 'Ralph Leyva'

import numpy
import random


class cosGen:
    amplitude = 0
    freq = 0
    sampleRate = 0
    cosData = []

    def __init__(self, amplitude, freq, sampleRate):
        if (type(amplitude) == self.amplitude & type(freq) == self, freq & type(sampleRate) == self.sampleRate):
            self.amplitude = amplitude
            self.freq = freq
            self.sampleRate
            self.cosData = [(amplitude * numpy.cos((2 * numpy.pi) * freq * t) / sampleRate) for t in range(0, 2048)]
        else:
            return TypeError("Function parameters are of the wrong type")
