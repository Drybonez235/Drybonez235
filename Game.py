Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Warrior(object):
	def __init__(self,name,attack,defense,health):
		self.name=name
		self.attack=attack
		self.defense=defense
		self.health=health

		
>>> Goblin= Warrior ("Bob" ,10,15,100)
>>> Elf= Warrior("Elon", 5,30,100)
>>> Archer= Warrior("Mike", 15,0,100)
>>> def Battle(*Warrior):
	Warrior1=Warrior[0]
	Warrior2=Warrior[1]
	if Warrior1.attack<Warrior2.defense:
		Warrior2.health= (Warrior2.health)-Damage(Warrior1,Warrior2)
		print(str(Warrior1.name),"did",str(Warrior1.attack),"to",str(Warrior2.name))
	else:
		print("nothing happened")

		
>>> def Damage(Warrior1,Warrior2):
	if Warrior1.attack<Warrior2.defense:
		return((Warrior2.defense)-(Warrior1.attack))

	
>>> def Health(*Warrior):
	Warrior1=Warrior[0]
	Warrior2=Warrior[1]
	Warrior3=Warrior[2]
	print((Warrior1.name),"has",(Warrior1.health),"health")
	print((Warrior2.name),"has",(Warrior2.health),"health")
	print((Warrior3.name),"has",(Warrior3.health),"health")

	
>>> print (hello)
