from typing import ClassVar
import math

class Vector (object):
    def __init__(self,x:float,y:float,z:float = 0.):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other:'Vector'):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self,other:'Vector'):
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
    def __mul__(self,value:float):
        return Vector(value*self.x, value*self.y, value*self.z)
    def __truediv__(self,value:float):
        return Vector(self.x/value, self.y/value, self.z/value)
    def dot(self,other:'Vector'):
        return self.x*other.x+self.y*other.y+self.z*other.z
    def magnitude(self):
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y and self.z==other.z
    def __repr__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'
    def unit(self):
        return self/self.magnitude()

class Point (object):
    def __init__(self,x:float,y:float,z:float = 0.):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other:Vector):
        return Point(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self,other):
        if isinstance(other, Vector):
            return Point(self.x-other.x,self.y-other.y,self.z-other.z)
        if isinstance(other, Point):
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        return None
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y and self.z==other.z
    def __repr__(self):
        return f'Point({self.x}, {self.y}, {self.z})'

if __name__ == "__main__":
    import unittest
    class testVector(unittest.TestCase):
        pass
        def testConstruction(self):
            v = Vector(1,2,3)
            self.assertEqual(v.x,1)
            self.assertEqual(v.y,2)
            self.assertEqual(v.z,3)
        def testDot(self):
            v = Vector(1,2,3)
            self.assertEqual(v.dot(Vector(1,0,0)), 1)
            self.assertEqual(v.dot(Vector(0,1,0)), 2)
            self.assertEqual(v.dot(Vector(0,0,1)), 3)
        def testMagnitude(self):
            v = Vector(1,2,3)
            self.assertEqual(v.magnitude(), math.sqrt(1+4+9))
        def testMult(self):
            v = Vector(1,2,3)
            v2 = v*2
            self.assertEqual(v2.x,2)
            self.assertEqual(v2.y,4)
            self.assertEqual(v2.z,6)
        def testDiv(self):
            v = Vector(1,2,3)
            v2 = v/2
            self.assertEqual(v2.x,0.5)
            self.assertEqual(v2.y,1)
            self.assertEqual(v2.z,1.5)
        def testAdd(self):
            v = Vector(1,2,3)
            vAdd = v+Vector(3,4,6)
            self.assertEqual(vAdd.x,4)
            self.assertEqual(vAdd.y,6)
            self.assertEqual(vAdd.z,9)
        def testSub(self):
            v = Vector(1,2,3)
            vAdd = v-Vector(3,3,3)
            self.assertEqual(vAdd.x,-2)
            self.assertEqual(vAdd.y,-1)
            self.assertEqual(vAdd.z,0)
    class testPoint(unittest.TestCase):
        def testConstruction(self):
            p = Point(1,2,3)
            self.assertEqual(p.x,1)
            self.assertEqual(p.y,2)
            self.assertEqual(p.z,3)
        def testAdd(self):
            p = Point(1,2,3)
            pAdd = p+Vector(3,4,6)
            self.assertEqual(pAdd.x,4)
            self.assertEqual(pAdd.y,6)
            self.assertEqual(pAdd.z,9)
        def testSub(self):
            p = Point(1,2,3)
            vAdd = p-Point(3,3,3)
            self.assertEqual(vAdd.x,-2)
            self.assertEqual(vAdd.y,-1)
            self.assertEqual(vAdd.z,0)
        def testunit(self):
            v=Vector(2,0,0)
            self.assertEqual(v.unit(),Vector(1,0,0))
    unittest.main()
        
        