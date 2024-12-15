from kinematics import Vector, Point

class Particle(object):
    def __init__(self, position:Point, velocity:Vector, mass:float):
        self.position = position
        self.velocity = velocity
        self.mass = mass

def simulation_step(deltaT:float, previous:Particle, force:Vector ):
    acceleration = force/previous.mass
    newVelocity = previous.velocity+acceleration*deltaT
    #take average of old and new velocity when calculating position
    newPosition = previous.position+(newVelocity+previous.velocity)/2.*deltaT
    return Particle(position=newPosition, velocity=newVelocity, mass=previous.mass)

if __name__ == "__main__":
    import unittest
    class testSimulation(unittest.TestCase):
        def testAtRest(self):
            start = Particle(position=Point(1,0,0), velocity=Vector(0,0,0), mass=1.0)
            nextStep = simulation_step(deltaT=1, previous=start, force=Vector(0,0,0))
            self.assertEqual(nextStep.position, Point(1,0,0))
            self.assertEqual(nextStep.velocity, Vector(0,0,0))
        def testInMotion(self):
            start = Particle(position=Point(1,0,0), velocity=Vector(0,1,0), mass=1.)
            nextStep = simulation_step(deltaT=1, previous=start, force=Vector(0,0,0))
            self.assertEqual(nextStep.position, Point(1,1,0))
            self.assertEqual(nextStep.velocity, Vector(0,1,0))
            nextStep = simulation_step(deltaT=1, previous=nextStep, force=Vector(0,0,0))
            self.assertEqual(nextStep.position, Point(1,2,0))
            self.assertEqual(nextStep.velocity, Vector(0,1,0))
        def testConstantAcceleration(self):
            start = Particle(position=Point(1,0,0), velocity=Vector(0,0,0), mass=1.)
            nextStep = simulation_step(deltaT=1, previous=start, force=Vector(1,0,0))
            self.assertEqual(nextStep.velocity, Vector(1,0,0))
            self.assertEqual(nextStep.position, Point(1.5,0,0))
            nextStep = simulation_step(deltaT=1, previous=nextStep, force=Vector(1,0,0))
            self.assertEqual(nextStep.velocity, Vector(2,0,0))
            self.assertEqual(nextStep.position, Point(3,0,0))
    unittest.main()
    