# 3D-Foucault-s-pendulum

With my physics TikTok account, I had a discussion with a flat-earther (a person who thinks that the Earth is flat, lol). We talked about the rotation of the Earth. I explained that the Foucault's pendulum demonstrates that the Earth is spinning, but he disagrees with this argument. Then, I challenged myself to do a simulation of the Foucault's pendulum in order to show him that the circular motion of the Earth causes the precession of the pendulum.

First, I took a pen and paper and I easily found the differential equations of motion pour the pendulum but i wanted it realistic so i wanted to find the ODE in spherical coordinates which was more complicated. By searching in papers on internet, I finally found the ODEs of $\theta$ and $\phi$ : 

$$
    \begin{array}{ll}
        \ddot{\theta} = 2\Omega \sin(l) \sin(\theta) \cos(\theta) \dot{\phi} -2\Omega \sin(\phi) \sin(\theta)^2 \cos(l) \dot{\phi} -\omega_0^2 \sin(\theta) + \sin(\theta) \cos(\theta) \dot{\phi}^2  \\
        \ddot{\phi} \sin(\theta) = -2 \Omega \sin(l) \sin(\theta) \dot{\theta} + 2 \Omega \sin(\phi) \sin(\theta)\cos(l) \dot{\theta} - 2 \cos(\theta) \dot{\theta} \dot{\phi} 
    \end{array}
$$

where : 

   - $\Omega = \frac{2\pi}{T}$ where T is the spinning time of Earth
   - $l$ is the lattitude
   - $\omega_0 = \frac{g}{L}$

From these ODEs, we determine our initial conditions for $\theta(t=0)$, $\phi(t=0)$, $\dot{\theta}(t=0)$ and $\dot{\phi}(t=0)$. Then, we solve these ODEs for $\theta$ and $\phi$ with the initial conditions with odeint from the scipy library.

    θ = solve_ODE(Eq_DP, initial_conditions, t_values, 0)
    φ = solve_ODE(Eq_DP, initial_conditions, t_values, 2)

From the spherical coordinates $\theta$ and $\phi$ (and $r=L$), we express the dynamics of the pendulum into cartesian coordinates $x,y,z$

$$
    \begin{array}{ll}
        x = L \sin(\theta) \cos(\phi) \\
        y = L \sin(\theta) \sin(\phi) \\
        z = -L \cos(\theta) \\
    \end{array}
$$

Then, we animate our pendulum in function of time by using FuncAnimation from the matplotlib.animation library.
The animation includes the dynamics of the pendulum and the path of the pendulum on the ground (in blue) to make the motion of the mass more visual.

For the following simulation, I took :

        L = 0.3  # Length of pendulum (m)
        g = 9.81  # Gravitational acceleration (m/s^2)
        T = 40  # Seconds in a day
        Ω = 2 * np.pi / T  # Pulsation of Earth's rotation
        l = np.radians(45)  # Latitude of the pendulum
        ω0 = np.sqrt(g / L)  # Pulsation of the pendulum

<img width="382" alt="image" src="https://github.com/HugoGW/3D-Foucault-s-pendulum/assets/140922475/fdfd8cbf-6733-4f20-a943-d05804a98e7e">

<img width="389" alt="image" src="https://github.com/HugoGW/3D-Foucault-s-pendulum/assets/140922475/94fccadb-7284-48f1-89ec-851ccf0ca225">

<img width="411" alt="image" src="https://github.com/HugoGW/3D-Foucault-s-pendulum/assets/140922475/971f1c71-be4e-416a-9d14-5cd83e737b91">

I could make my simulation more realistic by including a friction term that causes energy loss, decreasing the amplitude of the pendulum's motion.

PS : I don't know why, but I can't plot a rope for the pendulum between the origin $(0,0,0)$ and the mass $(x,y,z)$ so I plotted a hundred of little black dots between the origin and the mass that can be seen as a rope.
Here's the previous line code that doesn't work

    def animate(i):
        n = 8
    
        rope_line.set_data([0, x[n * i]], [0, y[n * i]])
        ax.plot([0, x[n*i]], [0, y[n*i]], [0, z[n*i]], color='black', linewidth=1)
        rope_line.set_3d_properties([0, z[n * i]])
    
        trajectory_line.set_data(x[:n * i], y[:n * i])
        trajectory_line.set_3d_properties(-1.1 * L)
        pendulum_bob.set_data(x[n * i], y[n * i])
        pendulum_bob.set_3d_properties(z[n * i])

