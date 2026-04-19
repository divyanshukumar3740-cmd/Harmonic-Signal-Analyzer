import numpy as np
from scipy.integrate import solve_ivp

def simulate_oscillator(m=1.0, c=0.5, k=4.0, x0=1.0, v0=0.0, t_end=20.0, t_steps=1000):
    def ode_system(t, y):
        x, v = y
        dxdt = v
        dvdt = (-c * v - k * x) / m
        return [dxdt, dvdt]

    t_span = (0, t_end)
    t_eval = np.linspace(0, t_end, t_steps)
    initial_conditions = [x0, v0]

    solution = solve_ivp(ode_system, t_span, initial_conditions, t_eval=t_eval, method='RK45')

    return solution.t, solution.y[0]