import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the ODE function dr/dt = r(1 - r) - gamma * r
def model(r, t, gamma):
    return r * r - gamma *(1-r)

# Define the initial condition
r0 = 0.6  # Initial value of r
alpha = 5
beta = 4
gamma = 0.3  # Gamma value
if gamma is None:
    gamma = beta / alpha

# Create an array of time values
t = np.linspace(0, 10, 100)  # Start at 0, end at 10, 100 points in between

# Solve the ODE
r = odeint(model, r0, t, args=(gamma,))

# Calculate n = 1 - r
n = 1 - r

# Plot both r and n in the same plot
plt.figure(figsize=(10, 8))

plt.plot(t, r, label='r(t)', color='blue', linewidth=2)
plt.plot(t, n, label='n(t) = (1 - r(t))', color='red', linestyle='--', linewidth=2)  # Plotting n = 1 - r
plt.xlabel('Time', fontsize=25)
plt.ylabel('Proportion', fontsize=25)
plt.title(r'$\gamma = $' + f'{gamma}', fontsize=25)  # Display gamma as a Greek symbol
plt.legend(fontsize=20)
plt.grid(True)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylim(-10, 10)  # Set y-axis range from 0 to 1
plt.tight_layout
plt.show()
