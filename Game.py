Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>>class Warrior(object):
	def __init__(self,name,attack,defense,health):
		self.name=name
		self.attack=attack
		self.defense=defense
		self.health=health

Goblin= Warrior ("Bob" ,10,15,100)
Elf= Warrior("Elon", 5,30,100)
Archer= Warrior("Mike", 15,0,100)

def Damage(Warrior):
    Warrior.attack=Warrior.attack*(randrange(1,2,.1))
    return Warrior.attack

def Mitigation(Warrior):
    Warrior.defense=Warrior.defense*(randrange(1,2,.1))
    return Warrior.defense
    
def Battle(*Warrior):
    Warrior1=Warrior[0]
    Warrior2=Warrior[1]
    Battle_Damage=Damage(warrior1)
    Battle_Mitigation=Mitigation(Warrior2)
    if Battle_Damage<Battle_Mitigation
        Warrior2.health= (Warrior2.health)+(Battle_Mitigation-Battle_Damage)
        print(str(Battle_Damage),"Damage")
        print(str(Warrior2.name),"has",(str(Warrior2.health)),"health remaining")
    elif Battle_Damage==Battle_Mitigation:
        print("draw")
    elif Battle_Damage>Battle_Mitigation:
        Warrior1.health= (Warrior1.health)-(Battle_Mitigation-Battle_Damage)
        

def Health(Warrior):
    if Warrior.health<0
        print(str(Warrior.name),"has",str(Warrior.health),"remaining")
    elif Warrior.health>=0
        print((Warrior.Name),"is Dead")
