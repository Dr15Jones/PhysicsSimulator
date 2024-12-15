from kinematics import Vector, Point
from simulation import Particle, simulation_step

particle = Particle(position=Point(0,0,0), velocity=Vector(1,0,0), mass=1.)

#for the first second, apply a constant acceleration in y
impulse = Vector(0,20,0)*particle.mass
gravity = Vector(0,-10,0)*particle.mass
time = 0
deltaT = 0.01 
while(particle.position.y >= 0.):
    time += deltaT
    if time < 1:
        force = impulse + gravity
    else:
        force = gravity
    particle = simulation_step(deltaT=deltaT, previous=particle, force=force)
    print(f"{particle.position.x}, {particle.position.y}")