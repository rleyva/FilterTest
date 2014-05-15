__author__ = 'Ralph Leyva'

import numpy as np
import random


def sinGen(self, freq):
    t = None
    sampleFreq = 44100
    return [np.cos((2 * np.pi * freq * t) / sampleFreq) for t in range(0, 2 * sampleFreq)]


def noiseGen():
    return sinGen(random.randrange(1, random.random, 1))


def sinAdd(sin1, sin2):
    return (sin1 + sin2)


def fftGen(sin1):
    return np.fft(sin1)