import numpy as np
import matplotlib.pyplot as plt
import os

def plot_results(t, x, freqs, amplitude, condition, damping_ratio, poles, filename="analysis.png"):
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    fig.suptitle(f"Harmonic Signal Analyzer  |  {condition}  |  ζ = {damping_ratio:.3f}", fontsize=14, fontweight='bold')

    axes[0, 0].plot(t, x, color='royalblue', linewidth=1.5)
    axes[0, 0].set_title("Time-Domain Signal")
    axes[0, 0].set_xlabel("Time (s)")
    axes[0, 0].set_ylabel("Displacement (m)")
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(0, color='black', linewidth=0.8, linestyle='--')

    axes[0, 1].plot(freqs, amplitude, color='crimson', linewidth=1.5)
    axes[0, 1].set_title("Frequency-Domain (FFT Spectrum)")
    axes[0, 1].set_xlabel("Frequency (Hz)")
    axes[0, 1].set_ylabel("Amplitude")
    axes[0, 1].grid(True, alpha=0.3)
    dominant_freq = freqs[np.argmax(amplitude)]
    axes[0, 1].axvline(dominant_freq, color='orange', linestyle='--', linewidth=1.2, label=f"Dominant: {dominant_freq:.3f} Hz")
    axes[0, 1].legend()

    real_parts = [p.real for p in poles]
    imag_parts = [p.imag for p in poles]
    axes[1, 0].scatter(real_parts, imag_parts, color='darkgreen', s=100, zorder=5, marker='x', linewidths=2.5)
    axes[1, 0].axvline(0, color='black', linewidth=1, linestyle='--')
    axes[1, 0].axhline(0, color='black', linewidth=1, linestyle='--')
    axes[1, 0].set_title("Pole-Zero Map (Laplace Domain)")
    axes[1, 0].set_xlabel("Real Axis")
    axes[1, 0].set_ylabel("Imaginary Axis")
    axes[1, 0].grid(True, alpha=0.3)
    for p in poles:
        axes[1, 0].annotate(f"  ({p.real:.2f}, {p.imag:.2f}j)", (p.real, p.imag), fontsize=8)

    envelope = np.exp(-abs(real_parts[0]) * t)
    axes[1, 1].plot(t, x, color='royalblue', linewidth=1.2, label='Signal')
    axes[1, 1].plot(t, envelope, color='orange', linewidth=1.2, linestyle='--', label='Decay envelope')
    axes[1, 1].plot(t, -envelope, color='orange', linewidth=1.2, linestyle='--')
    axes[1, 1].set_title("Signal with Decay Envelope")
    axes[1, 1].set_xlabel("Time (s)")
    axes[1, 1].set_ylabel("Displacement (m)")
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend()

    plt.tight_layout()
    os.makedirs("outputs", exist_ok=True)
    plt.savefig(f"outputs/{filename}", dpi=150, bbox_inches='tight')
    print(f"Plot saved to outputs/{filename}")
    print("Plot saved to outputs/analysis.png")
    plt.show()