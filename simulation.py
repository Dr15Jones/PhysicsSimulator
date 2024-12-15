from kinematics import Vector, Point

class Kinematics(object):
    def __init__(self, position:Point, velocity:Vector):
        self.position = position
        self.velocity = velocity

def simulation_step(deltaT:float, previous:Kinematics, mass: float, force:Vector ):
    acceleration = force/mass
    newVelocity = previous.velocity+acceleration*deltaT
    #take average of old and new velocity when calculating position
    newPosition = previous.position+(newVelocity+previous.velocity)/2.*deltaT
    return Kinematics(position=newPosition, velocity=newVelocity)

if __name__ == "__main__":
    import unittest
    class testSimulation(unittest.TestCase):
        def testAtRest(self):
            start = Kinematics(position=Point(1,0,0), velocity=Vector(0,0,0))
            nextStep = simulation_step(deltaT=1, previous=start, mass=1., force=Vector(0,0,0))
            self.assertEqual(nextStep.position, Point(1,0,0))
            self.assertEqual(nextStep.velocity, Vector(0,0,0))
        def testInMotion(self):
            start = Kinematics(position=Point(1,0,0), velocity=Vector(0,1,0))
            nextStep = simulation_step(deltaT=1, previous=start, mass=1., force=Vector(0,0,0))
            self.assertEqual(nextStep.position, Point(1,1,0))
            self.assertEqual(nextStep.velocity, Vector(0,1,0))
            nextStep = simulation_step(deltaT=1, previous=nextStep, mass=1., force=Vector(0,0,0))
            self.assertEqual(nextStep.position, Point(1,2,0))
            self.assertEqual(nextStep.velocity, Vector(0,1,0))
        def testConstantAcceleration(self):
            start = Kinematics(position=Point(1,0,0), velocity=Vector(0,0,0))
            nextStep = simulation_step(deltaT=1, previous=start, mass=1., force=Vector(1,0,0))
            self.assertEqual(nextStep.velocity, Vector(1,0,0))
            self.assertEqual(nextStep.position, Point(1.5,0,0))
            nextStep = simulation_step(deltaT=1, previous=nextStep, mass=1., force=Vector(1,0,0))
            self.assertEqual(nextStep.velocity, Vector(2,0,0))
            self.assertEqual(nextStep.position, Point(3,0,0))
    unittest.main()
    