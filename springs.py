from kinematics import Vector, Point
from simulation import Particle, simulation_step

#have two particles joined by a massless spring
particle1 = Particle(position=Point(-2.,0,0), velocity=Vector(0,1,0), mass=1.)
particle2 = Particle(position=Point( 2.,0,0), velocity=Vector(0,1,0), mass=1.)
#particle1 = Particle(position=Point(-1.,0,0), velocity=Vector(0,1,0), mass=1.)
#particle2 = Particle(position=Point( 1.,0,0), velocity=Vector(0,-1,0), mass=1.)

def springForce(p1:Particle, p2:Particle)->Vector :
    separation = p1.position-p2.position
    distance = separation.magnitude()
    restDistance = 3.
    diff = distance-restDistance
    k = 20. #Newton/meter
    return (separation/distance)*k*diff*-1

deltaT = 0.01 
while(particle1.position.y <= 5.):
    force = springForce(particle1,particle2)
    particle1 = simulation_step(deltaT=deltaT, previous=particle1, force=force/2)
    particle2 = simulation_step(deltaT=deltaT, previous=particle2, force=force/2*-1)
    print(f"{particle1.position.x}, {particle1.position.y}")