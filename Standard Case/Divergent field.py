import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the ODE function dr/dt = r(1 - r) - gamma * r
def model(r, t, gamma):
    return r * (1 - r) - gamma * r

# Create an array of time values
t = np.linspace(0, 15, 100)  # Start at 0, end at 10, 100 points in between
r0 = 0.1

# Define the parameter values to explore
gamma_values = [0.5 * k for k in range(5)]  # Adjust the range as needed
gamma_values.append(0.95)
gamma_values = sorted(gamma_values)

# Define different line styles
line_styles = ['-', '--', '-.', ':', (0, (3, 1, 1, 1)), (0, (5, 2))]

# Plot parameter sweep with different line styles
plt.figure(figsize=(12, 5))

for gamma, line_style in zip(gamma_values, line_styles):
    # Solve the ODE
    r = odeint(model, r0, t, args=(gamma,))

    # Calculate n = 1 - r
    n = 1 - r

    # Plot the solution for each gamma with different line styles
    plt.plot(t, r, label=f'γ={gamma:.2f}', linestyle=line_style)

plt.xlabel('Time')
plt.ylabel('r(t)')
plt.title('Parameter Sweep for ODE Solution with Different Line Styles')
plt.legend()
plt.grid(True)
plt.ylim(0, 1)
plt.show()
