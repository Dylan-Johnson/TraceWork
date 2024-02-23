# Plot the trace observations of a set of traces before and after a FFT
import trsfile
import numpy as np
import scipy.fft
import matplotlib.pyplot as plt

with trsfile.open('90x500xfloat.trs', 'r') as traces:
    for trace in traces:
        y = [value for value in trace]
        
        x=np.arange(0,len(y))
        y_fft = scipy.fft.fft(y)  

        plt.figure(1)
        plt.subplot(211)
        plt.plot(x, y)
        plt.subplot(212)
        plt.plot(x, 2*y_fft)
        plt.show()  