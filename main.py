import argparse
import numpy as np
from src.physics_engine import simulate_oscillator
from src.math_engine import apply_fft, analyze_stability
from src.visualizer import plot_results

def parse_args():
    parser = argparse.ArgumentParser(
        description="Harmonic Signal Analyzer — Simulate and analyze damped oscillator systems",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--mass",    type=float, default=1.0,  help="Mass (kg)")
    parser.add_argument("--damping", type=float, default=0.5,  help="Damping coefficient (N·s/m)")
    parser.add_argument("--spring",  type=float, default=4.0,  help="Spring constant (N/m)")
    parser.add_argument("--x0",      type=float, default=1.0,  help="Initial displacement (m)")
    parser.add_argument("--v0",      type=float, default=0.0,  help="Initial velocity (m/s)")
    parser.add_argument("--duration",type=float, default=20.0, help="Simulation duration (s)")
    parser.add_argument("--steps",   type=int,   default=1000, help="Number of time steps")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    t, x = simulate_oscillator(
        m=args.mass,
        c=args.damping,
        k=args.spring,
        x0=args.x0,
        v0=args.v0,
        t_end=args.duration,
        t_steps=args.steps
    )

    freqs, amplitude = apply_fft(t, x)
    poles, is_stable, damping_ratio, condition = analyze_stability(
        m=args.mass,
        c=args.damping,
        k=args.spring
    )

    print(f"\n{'='*45}")
    print(f"  Harmonic Signal Analyzer")
    print(f"{'='*45}")
    print(f"  Mass             : {args.mass} kg")
    print(f"  Damping coeff    : {args.damping} N·s/m")
    print(f"  Spring constant  : {args.spring} N/m")
    print(f"{'='*45}")
    print(f"  System condition : {condition}")
    print(f"  Damping ratio    : {damping_ratio:.4f}")
    print(f"  Stable           : {is_stable}")
    print(f"  Dominant freq    : {freqs[np.argmax(amplitude)]:.4f} Hz")
    print(f"{'='*45}\n")

    plot_results(t, x, freqs, amplitude, condition, damping_ratio, poles)