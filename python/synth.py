
import numpy as np
import sounddevice as sd

def generate_sine_wave(freq, duration, amplitude=1.0, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = amplitude * np.sin(2 * np.pi * freq * t)
    return waveform
