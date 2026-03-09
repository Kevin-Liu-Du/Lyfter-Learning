class Character():
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_status(self):
        print(f"Name: {self.name} \nHealth: {self.health}")

class Warrior():
    def __init__(self, strength):
        self.strength = strength

    def attack(self):
        print(f"Warrior attacks with strength {self.strength}.")

class Mage():
    def __init__(self, mana):
        self.mana = mana

    def cast_spell(self):
        print(f"Mage casts a spell using {self.mana} mana.")

class BattleMage(Character, Warrior, Mage):
    def __init__(self, name, health, strength, mana):
        Character.__init__(self, name, health)
        Warrior.__init__(self, strength)
        Mage.__init__(self, mana)



bm = BattleMage("Maria", 120, 40, 80)
bm.show_status()
bm.attack()
bm.cast_spell()
