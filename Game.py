Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class warrior(object):
    def __init__(self, Race, Name, Attack, Defense, Health):
        self.Race = Race
        self.Name = Name
        self.Attack = Attack
        self.Defense = Defense
        self.Health = Health


def battle(*warrior):
    def damage(Warrior):
        Warrior.Attack = warrior.Attack+1
        return Warrior.Attack
    def mitigation(Warrior):
        Warrior.Defense = warrior.Defense+1
        return warrior.Defense
    warrior1 = warrior[0]
    warrior2 = warrior[1]
    battle_damage = (damage(warrior1))
    battle_mitigation = (mitigation(warrior2))
    if battle_damage < battle_mitigation:
        warrior2.health = (warrior2.health + (battle_mitigation - battle_damage))
        print(str(battle_damage), "damage")
        print(str(warrior2.name), "has", str(warrior2.Health), "Health Remaining")
    elif battle_damage == battle_mitigation:
        print("Draw")
    elif battle_damage > battle_mitigation:
        warrior1.Health = warrior1.Health - (battle_mitigation - battle_damage)
        print(str(battle_mitigation), "Recoil was done")
        print(str(warrior1.name), "has", str(warrior2.Health), "Health Remaining")


def health(warrior):
    if warrior.Health < 0:
        print(str(warrior.Name), "has", str(warrior.Health), "remaining")
    else:
        print(warrior.name, "is dead")


Bob = warrior("Goblin", "Bob", 15, 10, 100)
Elon = warrior("Elf", "Elon", 10, 20, 100)
Mike = warrior("Man", "Mike", 20, 0, 100)
