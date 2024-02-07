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

From the spherical coordinates $\theta$ and $\phi$ (and $r=L$), we exprime the dynmaic of the pendulum into cartesian coordinates $x,y,z$

$$
    \begin{array}{ll}
        x = L \sin(\theta) \cos(\phi) \\
        y = L \sin(\theta) \sin(\phi) \\
        z = -L \cos(\theta) \\
    \end{array}
$$

Then, we animate our 2N angles in function of time by using FuncAnimation from the matplotlib.animation library.

https://github.com/HugoGW/Simple-and-double-Pendulums/assets/140922475/858d2216-4e0f-45c1-a99a-05b943aec61f

We could add dots to explicitly show the masses but I find it more elegant without them.

We could also plot the behavior of the 2 angles in their respective phase spaces, which could be interesting.
We could improve our model by considering friction.



