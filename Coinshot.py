from simulation import Particle, simulation_step, Vector, Point
import matplotlib.pyplot as plt
import math
Person=Particle(Point(0,1,0),Vector(0,0,0),mass=68)
Coin = Particle(Point(.5,1.1,0),Vector(0,0,0),mass=.05)
CoinshotForce=5
FGravCoin=Vector(0,-9.81*Coin.mass,0)
FGravPerson=Vector(0,-9.81*Person.mass,0)
CoinPosition=[]
PersonPosition=[]
while Coin.position.x<100 and Coin.position.y>0:
	FCoinshot=((Coin.position-Person.position).unit()*CoinshotForce)
	FSumCoin=FGravCoin+FCoinshot
	Coin=simulation_step(deltaT=.01,previous=Coin,force=FSumCoin)
	CoinPosition.append(Coin.position)
	if Person.position.y 
	FSumPerson=
	Person=simulation_step(deltaT=.01,previous=Person,force=FCoinshot*-1+Vector(0,FCoinshot.y,0))
	PersonPosition.append(Person.position)
	
plt.grid(True)
plt.title('Coinshot trajectory')

#CoinPlt = plt.plot([p.x for p in CoinPosition],[p.y for p in CoinPosition], lw=2, c='r')
PersonPlt= plt.plot([p.x for p in PersonPosition],[p.y for p in PersonPosition], lw=2, c='b')
plt.legend([PersonPlt[0]],['Person'], loc=4)
#plt.legend([CoinPlt[0],PersonPlt[0]],['Coin','Person'], loc=4)
plt.show()
