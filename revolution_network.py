from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np


def model(r, t, gamma, B):
    dr_dt = []
    for i in range(len(r)):
        s = 0
        for j in range(len(r)):
            s += B[i][j] * r[j]
        dri_dt = -gamma[i] * r[i] + (1 - r[i]) * s
        dr_dt.append(dri_dt)
    return dr_dt


num_cities = 5

# Initial values
p = 0.01 #ratio between big city and villages
total_r_propprtion = num_cities / 10
big_city = total_r_propprtion * p
if num_cities > 1:
    village = total_r_propprtion*(1 - p) / 10*(num_cities - 1)
r0 = [big_city] + [village for _ in range(num_cities - 1)]

# Number of people in city N_i
n_e = 20
N = [1000] + [140 - n_e * i for i in range(num_cities - 1)]

alpha_r = [10] + [3 for _ in range(num_cities - 1)]
alpha_n = [4 for _ in range(num_cities)]

matrix_size = num_cities
lambda_value = 0.1
B = [
    [N[j] * lambda_value / (N[i] * alpha_r[i]) if i != j else 1 for i in range(matrix_size)]
    for j in range(matrix_size)
]

gamma = [alpha_n[i] / alpha_r[i] for i in range(len(alpha_r))]

# Time points to solve the ODE
t = np.linspace(0, 100, 100)  # Adjust the time range accordingly

# Solve the ODE using odeint
solution = odeint(model, r0, t, args=(gamma, B))

# Plot the results with y-axis range from 0 to 1
for i in range(num_cities):
    plt.plot(t, solution[:, i], label=f'ppl. = {N[i]}')

plt.title(f'Revolutionary Proportions Over Time\nLambda = {lambda_value}')
plt.xlabel('Time')
plt.ylabel('Revolutionary Proportion')
plt.legend()
plt.ylim(-0.1, 1)
plt.grid(True)
plt.tight_layout
plt.show()
