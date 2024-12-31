from simulation import Particle, simulation_step, Vector, Point
import matplotlib.pyplot as plt
import math
def surface_force(forcesum:Vector,height:float,object:Particle):
	if forcesum.y<0 and object.position.y<=height:
		staticforce=-1*(forcesum.y)*.7 #coeffient of static friction
		if abs(forcesum.x)<staticforce: #check static force else apply kinetic force
			forcesum.x=0
		else:
			kineticforce=staticforce*.8
			if forcesum.x <0:
				forcesum.x+=kineticforce
			else:
				forcesum.x-=kineticforce
		forcesum.y=0
	return forcesum
def ground_collision(height:float,object:Particle):
	if object.position.y<height:
		object.position.y=height
		object.velocity.y=0
	return object

starting_height_coin=0.2
starting_height_person=1
mass_person=68
mass_coin=0.5
Person=Particle(Point(0,starting_height_person,0),Vector(0,0,0),mass=mass_person)
Coin = Particle(Point(.005,starting_height_coin,0),Vector(0,0,0),mass=mass_coin)
FGravCoin=Vector(0,-9.81*Coin.mass,0)
FGravPerson=Vector(0,-9.81*Person.mass,0)
CoinshotForce=1.1*(9.81*Person.mass)
CoinPosition=[]
PersonPosition=[]
airborn = False
while Coin.position.x<100 and (Coin.position.y>0 or not (airborn and Person.position.y<=starting_height_person)):
	FCoinshot=((Coin.position-Person.position).unit()*CoinshotForce)
	FSumCoin=FGravCoin+FCoinshot
	FSumPerson=FCoinshot*-1+FGravPerson
	#Surface force is checked includes normal and frictional forces
	FSumCoin=surface_force(FSumCoin,0,Coin)
	FSumPerson= surface_force(FSumPerson,starting_height_person,Person)
	if FSumPerson.y > 0:
		airborn = True
	#Update step
	Coin=simulation_step(deltaT=.01,previous=Coin,force=FSumCoin)
	Person=simulation_step(deltaT=.01,previous=Person,force=FSumPerson)
	#Collision with ground
	Coin=ground_collision(0,Coin)
	Person=ground_collision(starting_height_person,Person)
	# add to arry for plotting
	CoinPosition.append(Coin.position)
	PersonPosition.append(Person.position)
	
plt.grid(True)
fig, axs = plt.subplots(2)
fig.suptitle('Coinshot trajectory')
CoinPlt = axs[0].plot([p.x for p in CoinPosition],[p.y for p in CoinPosition], lw=2, c='r')
PersonPlt= axs[1].plot([p.x for p in PersonPosition],[p.y for p in PersonPosition], lw=2, c='b')
#plt.legend([PersonPlt[0]],['Person'], loc=4)
plt.legend([CoinPlt[0],PersonPlt[0]],['Coin','Person'], loc=4)
plt.xlabel("Horizontal position")
plt.ylabel("Vertical position")
#plt.gca().set_ylim([1,1.000001])
plt.show()
