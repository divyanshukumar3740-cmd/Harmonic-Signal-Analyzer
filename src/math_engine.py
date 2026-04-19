import numpy as np
from scipy.fft import fft, fftfreq
import scipy.signal as signal

def apply_fft(t, x):
    n = len(t)
    dt = t[1] - t[0]

    X = fft(x)
    freqs = fftfreq(n, dt)

    positive = freqs > 0
    freqs = freqs[positive]
    amplitude = (2 / n) * np.abs(X[positive])

    return freqs, amplitude

def analyze_stability(m=1.0, c=0.5, k=4.0):
    numerator = [1]
    denominator = [m, c, k]

    system = signal.TransferFunction(numerator, denominator)
    poles = system.poles

    is_stable = all(p.real < 0 for p in poles)
    damping_ratio = c / (2 * np.sqrt(m * k))

    if damping_ratio < 1:
        condition = "Underdamped"
    elif damping_ratio == 1:
        condition = "Critically Damped"
    else:
        condition = "Overdamped"

    return poles, is_stable, damping_ratio, condition