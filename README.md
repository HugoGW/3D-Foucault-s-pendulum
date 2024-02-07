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


Then, we choose our initial condition for our angles $\theta_1(t=0), \theta_2(t=0), \omega_1(t=0), \omega_2(t=0)$. 

In this code, I choose that my N double pendulums all have the same initial conditions except for $\displaystyle \theta_1^k(t=0) = \theta_1(t=0)\times k d\theta_1 ~~ \forall ~ k \in  {1,...,N}$.

Once every couple of angle [\theta_1^k, \theta_2^k] solved, we determine the position of the masses of the double pendulum with polar coordinates (by taking into account that the zero angle starts at $-\pi /2$ on the unit circle because $\vec{g} ~~ // -\vec{e}_y$: 

$$
    \begin{array}{ll}
        x_1^k = L_1 \sin(\theta_1^k) \\
        y_1^i = -L_1 \cos(\theta_1^k) \\
        x_2^i = x_1^k + L_2 \sin(\theta_2^k) \\
        y_2^i = y_1^k -L_2 \cos(\theta_2^k) \\
    \end{array}
$$

Then, we animate our 2N angles in function of time by using FuncAnimation from the matplotlib.animation library.

https://github.com/HugoGW/Simple-and-double-Pendulums/assets/140922475/858d2216-4e0f-45c1-a99a-05b943aec61f

We could add dots to explicitly show the masses but I find it more elegant without them.

We could also plot the behavior of the 2 angles in their respective phase spaces, which could be interesting.
We could improve our model by considering friction.



