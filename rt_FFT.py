import pyaudio
from matplotlib import pyplot
import numpy


def shapeTriangle(data):
    triangle = numpy.array(range(len(data) / 2) + range(len(data) / 2)[::-1]) + 1
    return data * triangle


def freqPlot(data, rate, freq, ffti, fftr):
    pyplot.subplot(4, 1, 1)
    pyplot.title("Original Data")
    pyplot.plot(numpy.arange(len(data)) / float(rate) * 1000, data, 'r-', alpha=1)
    pyplot.grid()
    pyplot.xlabel("Time (milliseconds)")
    pyplot.ylabel("Amplitude")

    pyplot.subplot(4, 1, 2)
    pyplot.title("Real FFT")
    pyplot.xlabel("Frequency (kHz)")
    pyplot.ylabel("Power")
    pyplot.grid()
    pyplot.plot(freq, fftr, 'b-', alpha=1)

    pyplot.subplot(4, 1, 3)
    pyplot.title("Imaginary FFT")
    pyplot.xlabel("Frequency (kHz)")
    pyplot.ylabel("Power")
    pyplot.grid()
    pyplot.plot(freq, ffti, 'g-', alpha=1)

    pyplot.subplot(4, 1, 4)
    pyplot.title("Real & Imaginary FFT")
    pyplot.xlabel("Frequency (kHz)")
    pyplot.ylabel("Power")
    pyplot.grid()
    pyplot.plot(freq, fftb, 'g-', alpha=1)

    pyplot.show()


def soundRec(blocks):
    data = []
    for i in range(0, blocks):
        data.append(numpy.fromstring(strm.read(1024), dtype=numpy.int16))
    return numpy.concatenate(data)


def freqGen(rate, data):
    fft = numpy.fft.fft(data)
    fftr = 10 * numpy.log10(abs(fft.real))[:len(data) / 2]
    ffti = 10 * numpy.log10(abs(fft.imag))[:len(data) / 2]
    fftb = 10 * numpy.log10(numpy.sqrt(fft.imag ** 2 + fft.real ** 2))[:len(data) / 2]
    freq = numpy.fft.fftfreq(numpy.arange(len(data)).shape[-1])[:len(data) / 2]
    freq = freq * rate / 1000


def updateGraph(plt, updatedData):
    assert isinstance(plt, pyplot)
    #assert isinstance(updatedData, tuple)


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

freqGen(RATE, soundRec(1))


