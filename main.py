
import numpy as np
from src.physics_engine import simulate_oscillator
from src.math_engine import apply_fft, analyze_stability
from src.physics_engine import simulate_oscillator
from src.math_engine import apply_fft, analyze_stability

if __name__ == "__main__":
    t, x = simulate_oscillator()
    print(f"Simulation complete. {len(t)} time steps generated.")

    freqs, amplitude = apply_fft(t, x)
    dominant_freq = freqs[np.argmax(amplitude)]
    print(f"Dominant frequency: {dominant_freq:.4f} Hz")

    poles, is_stable, damping_ratio, condition = analyze_stability()
    print(f"System condition: {condition}")
    print(f"Damping ratio: {damping_ratio:.4f}")
    print(f"Stable: {is_stable}")
    print(f"Poles: {poles}")