class Pokemon:
    def __init__(self, name, health, element):
        self.name = name
        self.health = health
        self.element = element

    def show_info(self):
        print(f"Pokemon: {self.name}")
        print(f"Health: {self.health}")
        print(f"Element: {self.element}")


class ElectricAttack:
    def __init__(self, voltage):
        self.voltage = voltage

    def thunder_attack(self):
        print(f"Electric attack with {self.voltage} volts!")


class FireAttack:
    def __init__(self, flame_power):
        self.flame_power = flame_power

    def fire_attack(self):
        print(f"Fire attack with power {self.flame_power}!")


class WaterAttack:
    def __init__(self, water_pressure):
        self.water_pressure = water_pressure

    def water_attack(self):
        print(f"Water attack with pressure {self.water_pressure}!")



class HybridPokemon(Pokemon, ElectricAttack, FireAttack):

    def __init__(self, name, health, element, voltage, flame_power):
        Pokemon.__init__(self, name, health, element)
        ElectricAttack.__init__(self, voltage)
        FireAttack.__init__(self, flame_power)

    def battle_style(self):
        print("This Pokemon can attack with both electricity and fire!")



pikazard = HybridPokemon("Pikazard", 120, "Electric/Fire", 90, 70)

pikazard.show_info()
pikazard.thunder_attack()
pikazard.fire_attack()
pikazard.battle_style()