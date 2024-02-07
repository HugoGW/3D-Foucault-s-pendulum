import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

L = 0.3  # Length of pendulum (m)
g = 9.81  # Gravitational acceleration (m/s^2)
T = 10  # Seconds in a day
Ω = 2 * np.pi / T  # Pulsation of Earth's rotation
l = np.radians(45)  # Latitude of the pendulum
ω0 = np.sqrt(g / L)  # Pulsation of the pendulum

# Function that solve ODE using odeint
def solve_ODE(equation, f0, t_values, colonne):
    solution = odeint(equation, f0, t_values)
    f_values = solution[:, colonne]
    return f_values

# Function representing the differential equations for the pendulum.
def Eq_DP(y, t):
    θ, dθdt, φ, dφdt = y

    # Differential equations of θ and φ

    d2θdt2 = 2 * Ω * np.sin(l) * np.sin(θ) * np.cos(θ) * dφdt - 2 * Ω * np.sin(φ) * np.sin(θ) ** 2 * np.cos(
        l) * dφdt - ω0 ** 2 * np.sin(θ) + np.sin(θ) * np.cos(θ) * dφdt ** 2

    d2φdt2 = (-2 * Ω * np.sin(l) * np.sin(θ) * dθdt + 2 * Ω * np.sin(φ) * np.sin(θ) * np.cos(
        l) * dθdt - 2 * np.cos(θ) * dθdt * dφdt) / np.sin(θ)

    return [dθdt, d2θdt2, dφdt, d2φdt2]

# Initial conditions
θ_0 = np.radians(60)
φ_0 = np.radians(0.0)
dθdt_0 = np.radians(0.0)
dφdt_0 = np.radians(0.0)
initial_conditions = [θ_0, φ_0, dθdt_0, dφdt_0]

# Time interval for the simulation
t_start = 0.0
t_end = 60
t_values = np.arange(t_start, t_end, 0.02)

# Solving the differential equations for the pendulum.
θ = solve_ODE(Eq_DP, initial_conditions, t_values, 0)
φ = solve_ODE(Eq_DP, initial_conditions, t_values, 2)

# Cartesian coordinates for the pendulum
x = L * np.sin(θ) * np.cos(φ)
y = L * np.sin(θ) * np.sin(φ)
z = -L * np.cos(θ)

# Number of masses
n = 100

# Create a 3D figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-L, L])
ax.set_ylim([-L, L])
ax.set_zlim([-L, 0])

# Initialize the trajectory line, pendulum bob, and rope
trajectory_line, = ax.plot([], [], [], color='blue')
pendulum_bob, = ax.plot([], [], [], color='red', marker='o', markersize=10)
rope = [ax.plot([], [], [], color='black', marker='o', markersize=1)[0] for _ in range(n)]

# Animation function
def animate(i):
    trajectory_line.set_data(x[:i], y[:i])
    trajectory_line.set_3d_properties(-1.1 * L)
    pendulum_bob.set_data(x[i], y[i])
    pendulum_bob.set_3d_properties(z[i])

    # Update the position of additional masses on the rope
    for j in range(n):
        # Calculate position
        x_additional = (L-j*L/n) * np.sin(θ[i]) * np.cos(φ[i])
        y_additional = (L-j*L/n) * np.sin(θ[i]) * np.sin(φ[i])
        z_additional = -(L-j*L/n) * np.cos(θ[i])

        # Update the position of the additional mass
        rope[j].set_data(x_additional, y_additional)
        rope[j].set_3d_properties(z_additional)


# Animate the trajectory
ani = FuncAnimation(fig, animate, frames=len(t_values), interval=1)

plt.show()
