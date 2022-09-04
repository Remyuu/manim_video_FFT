import numpy as np                      # NumPy, abbreviated as np
import matplotlib.pyplot as plt         # MatplotLib PyPlot module, abbreviated as plt
from matplotlib import animation, rc    # MatplotLib animation module

from scipy import signal                # SciPy's signal module, for DSP functions
import soundfile as sf                  # Switching to the soundfile module for reading and writing soundfiles

import IPython.display as ipd           # Interactive Python display module, for playing sounds
from IPython.display import HTML        # For displaying animations


def plotSpectrogram(sig, fs, win='hann', nseg=512, olap=256, fft_len=512):
   f1, t1, Sxx = signal.spectrogram(
      sig, fs, window=win, nperseg=nseg, noverlap=olap, nfft=fft_len)

    fig = plt.figure(figsize=(16, 6))

    plt.pcolormesh(t1, f1, 20*np.log10(np.abs(Sxx)))
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (sec)')
    return fig, plt





