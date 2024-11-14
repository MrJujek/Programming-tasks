import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io.wavfile import write
from scipy.fft import fft
import pandas as pd

class Generator:
    def __init__(self,f,fs,a,t):
        self.f=f
        self.fs=fs
        self.a=a
        self.T =1/f
        self.t=t

    def ti(self):
        return np.linspace(0, self.t, self.t * self.fs)

    def sawtooth(self):
        return 0.5*(1+np.mod(self.ti()*self.f,1))

    def sine(self):
        return self.a * np.sin(2 * np.pi * self.f * self.ti())

    def square(self):
        return self.a*signal.square(2*np.pi*self.f*self.ti())

    def triangle(self):
        return self.a*signal.sawtooth(2*np.pi*self.f*self.ti(), width=0.5)

    def white_noise(self):
        return self.a*np.random.normal(0,self.a,len(self.ti()))
    
    def draw(self, func, limit):
        plt.plot(self.ti(), func)
        plt.xlim(0, limit)
        plt.show()

    def fourier_transform(self, y):
        N = len(self.ti())
        dt = self.ti()[1] - self.ti()[0]
        yf = 2.0 / N * np.abs(fft(y)[0:N // 2])
        xf = np.fft.fftfreq(N, d=dt)[0:N // 2]
        return xf, yf
    
    def fourier_chart(self, data):
        xf , yf = test.fourier_transform(data)
        plt.plot(xf, yf)
        plt.show()

    def save_wav(self, data):
        audio_data = np.int16(data * 2**15)
        write("saved.wav", self.fs, audio_data)

    def save_fourier(self, data):
        xf , yf = test.fourier_transform(data)
        df = pd.DataFrame({'xf': xf, 'yf': yf})
        df.to_csv('output.csv', index=False)

test = Generator(440, 44100, 0.1, 5)
data = test.sawtooth()
test.draw(data, 0.010)
test.save_wav(data)
test.save_fourier(data)
test.fourier_chart(data)
