Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>>class Warrior(object):
class Warrior(object):
    def __init__(self,Race,Name,Attack,Defense,Health):
        self.Race=Race
        self.Name=Name
        self.Attack=Attack
        self.Defense=Defense
        self.Health=Health

Bob= Warrior("Goblin","Bob",15,10,100)
Elon= Warrior("Elf","Elon",10,20,100)
Mike= Warrior("Man","Mike",20,0,100)

def Damage(Warrior):
    Warrior.attack=Warrior.attack*(randrange(1,2,.1))
    return Warrior.attack

def Mitigation(Warrior):
    Warrior.defense=Warrior.defense*(randrange(1,2,.1))
    return Warrior.defense
    
def Battle(*Warrior: object) -> object:
    Warrior1=Warrior[0]
    Warrior2=Warrior[1]
    Battle_Damage=(Damage(Warrior1))
    Battle_Mitigation=(Mitigation(Warrior2))
    if Battle_Damage<Battle_Mitigation
        Warrior2.health= (Warrior2.health+(Battle_Mitigation-Battle_Damage))
        print(str(Battle_Damage),"Damage")
        print(str(Warrior2.name),"has",str(Warrior2.Health),"Health Remaning")
    elif Battle_Damage==Battle_Mitigation
        print("Draw")
    elif Battle_Damage>Battle_Mitigation
        Warrior1.Health= Warrior1.Health-(Battle_Mitigation-Battle_Damage)
        print(str(Battle_Mitigation),"Recoil was done")
        print(str(Warrior1.name),"has",str(Warrior2.Health),"Health Remaining"))
        

def Health(Warrior):
    if Warrior.health<0
        print(str(Warrior.name),"has",str(Warrior.health),"remaining")
    elif Warrior.health>=0
        print((Warrior.Name),"is Dead")
