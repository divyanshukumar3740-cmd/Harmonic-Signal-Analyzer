from src.physics_engine import simulate_oscillator

if __name__ == "__main__":
    t, x = simulate_oscillator()
    print(f"Simulation complete. {len(t)} time steps generated.")
    print(f"Time range: 0 to {t[-1]:.1f}s")
    print(f"Max displacement: {max(x):.4f}m")