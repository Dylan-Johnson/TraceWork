# Demonstrate example of a discrete FFT on simple data
import scipy.fft
import numpy as np
import matplotlib.pyplot as plt

y = np.exp(2j * np.pi * np.arange(8) / 8)
x=np.arange(0,len(y))

# plt.plot(x, y)
# plt.show()

y_fft = scipy.fft.fft(y)
y_fft

# plt.plot(x, y_fft)
# plt.show()

plt.figure(1)
plt.subplot(211)
plt.plot(x, y)
plt.subplot(212)
plt.plot(x, 2*y_fft)
plt.show()