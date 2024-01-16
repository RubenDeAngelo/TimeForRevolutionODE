import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the ODE system for r1 and r2
def model(z, t, gamma1, gamma2, beta12, beta21):
    r1, r2 = z
    dr1dt = r1 * (1 - r1) - gamma1 * r1 + beta12 * r2 * (1 - r1)
    dr2dt = r2 * (1 - r2) - gamma2 * r2 + beta21 * r1 * (1 - r2)
    return [dr1dt, dr2dt]

# Define the initial conditions and parameters
N1 = 1.5
N2 = 0.5
r1_0 = 0.1
r2_0 = 0.1
gamma1 = 0.2
gamma2 = 1.5
beta12 = 0.2 * N2
beta21 = 0.1 * N1

# Create an array of time values
t = np.linspace(0, 15, 1000)

# Solve the ODE system
z0 = [r1_0, r2_0]
z = odeint(model, z0, t, args=(gamma1, gamma2, beta12, beta21))
r1, r2 = z[:, 0], z[:, 1]

# Calculate n1 = 1 - r1 and n2 = 1 - r2
n1 = 1 - r1
n2 = 1 - r2

# Plot r1 with n1 and r2 with n2 in subplots
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(t, r1, label='r1(t)', color='blue')
plt.plot(t, n1, label='n1(t) (1 - r1(t))', color='orange', linestyle='--')
if gamma1 < 1:
    plt.axhline(y=1-gamma1, color='lightcoral', linestyle='--', label='neutral convergence')
else:
    plt.axhline(y=0, color='lightcoral', linestyle='--', label='neutral convergence')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Solution for $r_1(t)$ and $n_1(t) = 1 - r_1(t)$')

# Dynamic placement of text with bounding box
plt.annotate(r'$\gamma_1 = {}$'.format(gamma1), xy=(1.6, 0.85), fontsize=12,
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='white', alpha=0.7))
plt.annotate(r"$\beta_{12}$ = " + str(beta12), xy=(1.6, 0.75), fontsize=12,
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='white', alpha=0.7))
plt.annotate(r'$N_{1}$ = ' + str(N1), xy=(1.6, 0.65), fontsize=12,
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='white', alpha=0.7))

plt.legend()
plt.grid(True)
plt.ylim(-0.1, 1)

plt.subplot(2, 1, 2)
plt.plot(t, r2, label='r2(t)', color='blue')
plt.plot(t, n2, label='n2(t) (1 - r2(t))', color='orange', linestyle='--')
if gamma2 < 1:
    plt.axhline(y=1-gamma2, color='lightcoral', linestyle='--', label='neutral convergence')
else:
    plt.axhline(y=0, color='lightcoral', linestyle='--', label='neutral convergence')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Solution for $r_2(t)$ and $n_2(t) = 1 - r_2(t)$')

# Dynamic placement of text with bounding box
plt.annotate(r'$\gamma_2 = {}$'.format(gamma2), xy=(1, 0.5), fontsize=12,
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='white', alpha=0.7))
plt.annotate(r"$\beta_{21}$ = " + str(beta21), xy=(1, 0.4), fontsize=12,
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='white', alpha=0.7))
plt.annotate(r'$N_{2}$ = ' + str(N2), xy=(1, 0.3), fontsize=12,
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='white', alpha=0.7))

plt.legend()
plt.grid(True)
plt.ylim(-0.1, 1)

plt.tight_layout()
plt.show()
