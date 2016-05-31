# Simulating Linear Momentum

The primary focus of this project was to build a robust system for simulating linear momentum interactions between particles. Previously I had attempted a simulation like this, but I hadn't considered the movement of the particles inbetween the discrete times at which the computer applies the laws of physics to the system. 

The following is a series of images that show the mathematical framework implemented in `HandleParticleCollisions.py`. The premise is that given the time elapsed since last application of the laws of physics, we can describe what the particles should have been
doing since then and adjust for any misbehaviour.

![working1](https://raw.githubusercontent.com/DylanCope/Linear-Momentum-Simulation/master/maths-workings/workings1.jpg)
![working2](https://raw.githubusercontent.com/DylanCope/Linear-Momentum-Simulation/master/maths-workings/workings2.jpg)

I wanted particles to behave similarly when they interacted with the boundaries of the view, so I set up a similar problem for
bouncing off lines described by arbitrary vector equations. This is implemented in `HandleBoundsCollisions.py`

![working1](https://raw.githubusercontent.com/DylanCope/Linear-Momentum-Simulation/master/maths-workings/workings3.jpg)
![working2](https://raw.githubusercontent.com/DylanCope/Linear-Momentum-Simulation/master/maths-workings/workings4.jpg)

## Optimising Collision Checks

The assumption here is that between frames it's most likely not neccessary to check for collisions between every possible pair
of particles, so instead a "sweep line" algorithm (https://en.wikipedia.org/wiki/Sweep_line_algorithm) can be implemented to dramatically improve performance. In this project I've gotten so far as implementing a standard sweep line approach for detecting line intersects, however it hasn't been specialised to the desired purpose. To properly implement the algorithm it would need to be remodeled to find intersections between oblongs at arbitrary positions and rotations.
