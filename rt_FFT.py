from matplotlib import pyplot
import collections
import numpy


def shapeTriangle(data):
    triangle = numpy.array(range(len(data) / 2) + range(len(data) / 2)[::-1]) + 1
    return data * triangle


def freqPlot(data, rate, freq, fftr, ffti, fftb):
    # Graphs the data

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


def soundRec(strm, blocks):
    # Function is called to begin recording sound
    # ---------------Input Vars---------------------
    # blocks: The number if blocks that you want to
    #         record.

    data = []
    for i in range(0, blocks):
        data.append(numpy.fromstring(strm.read(1024), dtype=numpy.int16))
    return numpy.concatenate(data)


def freqGen(rate, data):
    # Function is called to generate FFT data
    #-------------Input Vars-------------------
    # rate: The sampling rate
    # data: The data that you are sampling (sound recording)

    fft = numpy.fft.fft(data)  # Calculates the FFT
    fftr = 10 * numpy.log10(abs(fft.real))[:len(data) / 2]  # Calculates the real portion of the FFT
    ffti = 10 * numpy.log10(abs(fft.imag))[:len(data) / 2]  # Calculates the img portion of the FFT
    fftb = 10 * numpy.log10(numpy.sqrt(fft.imag ** 2 + fft.real ** 2))[:len(data) / 2]  # Calculates the mag of the FFT
    freq = numpy.fft.fftfreq(numpy.arange(len(data)).shape[-1])[:len(data) / 2]  # Generates the freq resp of the FFT
    freq = freq * rate / 1000  # Rescales the freq
    freqData = collections.namedtuple('freqData', 'fft fftb ffti fftr freq')
    return freqData(fft, fftb, ffti, fftr, freq)


def updateGraph(plt, wvData, freqData):
    assert isinstance(plt, pyplot)
    assert isinstance(wvData, [])
    plt.ion()  # Enables interactive mode
    plt.plot(freqData, wvData)  # Updates the graph data
    plt.draw()  # Renders graph
    return plt




