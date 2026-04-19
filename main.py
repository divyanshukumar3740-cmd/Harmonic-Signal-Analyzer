import numpy as np
from src.physics_engine import simulate_oscillator
from src.math_engine import apply_fft, analyze_stability
from src.visualizer import plot_results

if __name__ == "__main__":
    t, x = simulate_oscillator()
    freqs, amplitude = apply_fft(t, x)
    poles, is_stable, damping_ratio, condition = analyze_stability()

    print(f"System condition : {condition}")
    print(f"Damping ratio    : {damping_ratio:.4f}")
    print(f"Stable           : {is_stable}")
    print(f"Dominant freq    : {freqs[np.argmax(amplitude)]:.4f} Hz")

    plot_results(t, x, freqs, amplitude, condition, damping_ratio, poles)