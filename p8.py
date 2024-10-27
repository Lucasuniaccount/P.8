from abc import ABC, abstractmethod

class Armour(ABC):
    def __init__(self, material, defensiveness, toughness, durability):
        self.material = material
        self.defensiveness = defensiveness
        self.toughness = toughness
        self.durability = durability
        self.protection = self.calculate_protection()

    @abstractmethod
    def calculate_protection(self):
        pass

    def reduce_durability(self, amount):
        self.durability = max(0, self.durability - amount)

    def repair_durability(self, amount):
        self.durability += amount

    def __str__(self):
        return (f"{self.material} Armour: Defensiveness = {self.defensiveness}, "
                f"Toughness = {self.toughness}, Durability = {self.durability}, "
                f"Protection = {self.protection}")

class Helmet(Armour):
    def calculate_protection(self):
        if self.durability > 0:
            return self.defensiveness + (self.toughness * 0.5)
        return 0

class Chestplate(Armour):
    def calculate_protection(self):
        if self.durability > 0:
            return self.defensiveness + (self.toughness * 0.75)
        return 0

class Leggings(Armour):
    def calculate_protection(self):
        if self.durability > 0:
            return self.defensiveness + (self.toughness * 0.7)
        return 0

class Boots(Armour):
    def calculate_protection(self):
        if self.durability > 0:
            return self.defensiveness + (self.toughness * 0.6)
        return 0

helmet = Helmet("Iron", defensiveness=5, toughness=2, durability=50)
chestplate = Chestplate("Diamond", defensiveness=8, toughness=3, durability=80)
leggings = Leggings("Gold", defensiveness=6, toughness=1, durability=40)
boots = Boots("Leather", defensiveness=2, toughness=0.5, durability=20)

print(helmet)
print(chestplate)
print(leggings)
print(boots)
