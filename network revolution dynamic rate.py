from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np

def model(r, t, gamma, B):
    dr_dt = []
    for i in range(len(r)):
        s = 0
        for j in range(len(r)):
            s += B[i][j] * r[j]
        dri_dt = -gamma[i] * (1-r[i]) +  r[i] * s
        dr_dt.append(dri_dt)
    return dr_dt

num_cities = 1

# Initial values
p = 7  # ratio between big city and villages
total_r_propprtion = num_cities / 10
big_city = total_r_propprtion * p
if num_cities > 1:
    village = total_r_propprtion * (1 - p) / 10 * (num_cities - 1)
r0 = [big_city] + [village for _ in range(num_cities - 1)]

# Number of people in city N_i
n_e = 50
N = [1000] + [200 - n_e * i for i in range(num_cities - 1)]

alpha_r = [5] + [3 for _ in range(num_cities - 1)]
alpha_n = [4 for _ in range(num_cities)]

matrix_size = num_cities

lambda_values = [[1,3,0],
                 [3,1,4],
                 [0,1,1]]
#lambda_values = [[1, 0.8, 10.5,0],
#                [10,1,0,0],
#                [0,0,1,8],
#                 [0,0,15,1]]


#B = [
#    [N[j] * lambda_values[i][j] / (N[i] * alpha_r[i]) if i != j else 1 for i in range(matrix_size)]
#    for j in range(matrix_size)
#]
B = np.array([
    [N[j] * lambda_values[i][j] / (N[i] * alpha_r[i]) if i != j else 1 for j in range(matrix_size)]
    for i in range(matrix_size)
])

gamma = [np.round(alpha_n[i] / alpha_r[i], 2) for i in range(len(alpha_r))]

# Time points to solve the ODE
t = np.linspace(0, 20, 100)  # Adjust the time range accordingly

# Solve the ODE using odeint
solution = odeint(model, r0, t, args=(gamma, B))

# Plot the results with y-axis range from 0 to 1
plt.figure(figsize=(10, 8))
for i in range(num_cities):
    color = plt.plot(t, solution[:, i], label=f'city {i+1}', linewidth=2)[0].get_color()
    """
    if gamma[i] < 1:
        plt.axhline(y=1 - gamma[i], color=color, linestyle='--', label=f'city {i+1} neutral equil.')
    else:
        plt.axhline(y=0, color=color, linestyle='--', label=f'city {i+1} neutral equil.')
    """

plt.title(f'Revolutionary Proportions Over Time', fontsize=25)
plt.xlabel('Time', fontsize=25)
plt.ylabel('Revolutionary Proportion', fontsize=25)
plt.legend(fontsize=20)
plt.ylim(-10, 10)
plt.grid(True)
plt.tight_layout()
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()

for i in range(num_cities):
    last_y_value = solution[-1, i]
    print(f"City {i + 1}: {last_y_value}")
    print("ppl. =", N[i], " gamma= ", gamma[i])

print("lambda:", lambda_values)
print("B:", B)