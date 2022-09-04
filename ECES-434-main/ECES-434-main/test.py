import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
import IPython.display as ipd

import librosa
from scipy import signal

from IPython.display import HTML
import scipy

yy44,fs44 = librosa.load('ECES-434-main/ECES-434-main/003.wav',sr=None)
ipd.Audio(yy44,rate=fs44)

t = np.arange(len(yy44)) / fs44
plt.plot(t,yy44)
fig = plt.figure(1,1)
plt.xlabel('Time(sec)')

f1, t1, Sxx = signal.spectrogram(yy44, fs44, window='hann', nperseg=2048, noverlap=1024, nfft=4096)

fig = plt.figure(figsize=(16,6))

plt.pcolormesh(t1, f1, 20*np.log10(np.abs(Sxx)))
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (sec)')

plt.xlim(0,5)
#plt.ylim(0,2000)

plt.show()


########################


yy11,fs11 = librosa.load(r'ECES-434-main/ECES-434-main/003.wav',sr=None)
ipd.Audio(yy11,rate=fs11)

def plotSpectrogram(sig, fs, win='hann', nseg=512, olap=256, fft_len=512):
  f1, t1, Sxx = signal.spectrogram(sig, fs, window=win, nperseg=nseg, noverlap=olap, nfft=fft_len)

  plt.figure(figsize=(16,6))

  plt.pcolormesh(t1, f1, 20*np.log10(np.abs(Sxx)))
  plt.ylabel('Frequency (Hz)')
  plt.xlabel('Time (sec)')
  return plt

plt1 = plotSpectrogram(yy11, fs11)
plt1.ylim(0,10000)
plt1.show()

yy11_44a = np.repeat(yy11,4)
ipd.Audio(yy11_44a,rate=44100)

plt.plot(yy11_44a[5000:5200])

plt2 = plotSpectrogram(yy11_44a, fs44)
plt2.ylim(0,20000)
plt2.show()


n_o = 0
f_size = 2048 * 2
n_hop = f_size / 2
N_fft = 4096 * 2
f = np.arange(N_fft) * fs44 / N_fft

# First set up the figure, the axis, and the plot element we want to animate
def setup(x_lim=(0,1000), y_lim=(-10,500)):
  fig = plt.figure(figsize=(14,6))
  ax = plt.axes(xlim=x_lim,ylim=y_lim)
  plt.close()   # Don't output the final figure separately
  line, = ax.plot([], [])
  return fig, line

# initialization function: plot the background of each frame
def init():
    #line, = ax.plot([], [])
    line.set_data([], [])
    return (line,)

# animation function. This is called sequentially  
def animate(i, sig):
    n1 = int(n_o + n_hop*i)
    n2 = int(n_o + n_hop*i + f_size)
    print(i)
    x_i = sig[n1:n2]
    X_i = np.abs(scipy.fft.fft(x_i * np.hanning(len(x_i))))
    xf = scipy.fft.fftfreq(4096,1/44100)
    X_mag = 20*np.log(np.abs(X_i))

    line.set_data(xf, X_i)
    return (line,)  

fig, line = setup()
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=480, fargs=(yy11_44a,), interval=1000/60, blit=True)
anim.save('2.mp4')