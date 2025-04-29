import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter

L = 67
g = 9.81
T = np.inf #1200
Ω = 2 * np.pi / T
l = np.radians(45)
ω0 = np.sqrt(g / L)

def Eq_DP(y, t):
    θ, dθdt, φ, dφdt = y
    d2θdt2 = 2 * Ω * np.sin(l) * np.sin(θ) * np.cos(θ) * dφdt \
             - 2 * Ω * np.sin(φ) * np.sin(θ)**2 * np.cos(l) * dφdt \
             - ω0**2 * np.sin(θ) + np.sin(θ) * np.cos(θ) * dφdt**2
    d2φdt2 = (-2 * Ω * np.sin(l) * np.cos(θ) * dθdt \
              + 2 * Ω * np.sin(φ) * np.sin(θ) * np.cos(l) * dθdt \
              - 2 * np.cos(θ) * dθdt * dφdt) / np.sin(θ)
    return [dθdt, d2θdt2, dφdt, d2φdt2]

# Conditions initiales
θ_0 = np.radians(60)
φ_0 = np.radians(0.0)
dθdt_0 = np.radians(0.0)
dφdt_0 = np.radians(0.2)
initial_conditions = [θ_0, dθdt_0, φ_0, dφdt_0]

# Temps
t_values = np.arange(0.0, 60, 0.1)
solution = odeint(Eq_DP, initial_conditions, t_values)
θ = solution[:, 0]
φ = solution[:, 2]

# Conversion sphérique -> cartésien
x = L * np.sin(θ) * np.cos(φ)
y = L * np.sin(θ) * np.sin(φ)
z = -L * np.cos(θ)

# Setup graphique
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-L, L])
ax.set_ylim([-L, L])
ax.set_zlim([-L, 0])

trajectory_line, = ax.plot([], [], [], color='blue')
pendulum_bob, = ax.plot([], [], [], color='red', marker='o', markersize=10)
rope_line, = ax.plot([], [], [], color='black')

def animate(i):
    trajectory_line.set_data(x[:i], y[:i])
    trajectory_line.set_3d_properties(-1.1 * L)
    pendulum_bob.set_data([x[i]], [y[i]])
    pendulum_bob.set_3d_properties([z[i]])
    rope_line.set_data([0, x[i]], [0, y[i]])
    rope_line.set_3d_properties([0, z[i]])

ani = FuncAnimation(fig, animate, frames=len(t_values), interval=1)
output_path = "/home/hugo-alexandre/pCloudDrive/Python/code_python_1m2p/Pendulums/Foucault's pendulum/Foucault_Pendulum.mp4"

writer = FFMpegWriter(fps=30, metadata=dict(artist='Hugo Alexandre'), bitrate=1800)
ani.save(output_path, writer=writer)
plt.show()
