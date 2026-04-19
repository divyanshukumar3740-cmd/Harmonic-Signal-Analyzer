\# Harmonic Signal Analyzer



A Python-based signal processing tool that simulates damped harmonic oscillator systems, applies Fourier and Laplace transform techniques, and visualizes results across time and frequency domains.



\## Overview



This project bridges \*\*computational physics\*\* and \*\*signal processing\*\* by:



\- Numerically solving second-order linear ODEs to simulate oscillator motion

\- Applying \*\*Fast Fourier Transform (FFT)\*\* to decompose signals into frequency components

\- Using \*\*Laplace Transform\*\* pole-zero analysis to classify system stability

\- Generating 4-panel diagnostic plots for every simulation



\## Physics Model



The system models a damped harmonic oscillator governed by:



&#x20;   m·(d²x/dt²) + c·(dx/dt) + k·x = 0



| Parameter | Symbol | Unit |

|-----------|--------|------|

| Mass | m | kg |

| Damping coefficient | c | N·s/m |

| Spring constant | k | N/m |

| Displacement | x | m |



\## Sample Output



\### Underdamped System (m=1, c=0.5, k=4)

!\[Underdamped](outputs/underdamped\_analysis.png)



\### Overdamped System (m=1, c=4, k=2)

!\[Overdamped](outputs/overdamped\_analysis.png)



\## Project Structure



&#x20;   Harmonic-Signal-Analyzer/

&#x20;   │

&#x20;   ├── src/

&#x20;   │   ├── physics\_engine.py

&#x20;   │   ├── math\_engine.py

&#x20;   │   └── visualizer.py

&#x20;   │

&#x20;   ├── tests/

&#x20;   ├── outputs/

&#x20;   ├── main.py

&#x20;   ├── requirements.txt

&#x20;   └── README.md



\## Setup



&#x20;   git clone https://github.com/YOUR\_USERNAME/Harmonic-Signal-Analyzer.git

&#x20;   cd Harmonic-Signal-Analyzer



&#x20;   python -m venv venv

&#x20;   venv\\Scripts\\activate



&#x20;   pip install -r requirements.txt



\## Usage



&#x20;   # Default run

&#x20;   python main.py



&#x20;   # Custom parameters

&#x20;   python main.py --mass 1.0 --damping 0.5 --spring 4.0 --duration 20



&#x20;   # See all options

&#x20;   python main.py --help



\## CLI Options



| Argument | Default | Description |

|----------|---------|-------------|

| `--mass` | 1.0 | Mass in kg |

| `--damping` | 0.5 | Damping coefficient (N·s/m) |

| `--spring` | 4.0 | Spring constant (N/m) |

| `--x0` | 1.0 | Initial displacement (m) |

| `--v0` | 0.0 | Initial velocity (m/s) |

| `--duration` | 20.0 | Simulation time (s) |

| `--steps` | 1000 | Number of time steps |



\## System Classification



| Condition | Damping Ratio (ζ) |

|-----------|-------------------|

| Underdamped | ζ < 1 |

| Critically Damped | ζ = 1 |

| Overdamped | ζ > 1 |



Damping ratio: `ζ = c / (2·√(m·k))`



\## Tech Stack



\- \*\*Python 3.10+\*\*

\- `numpy` — numerical computation

\- `scipy` — ODE solver, FFT, transfer function analysis  

\- `matplotlib` — visualization

