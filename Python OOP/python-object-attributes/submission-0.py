class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy
    def modify_hunger(self, value=int):
        self.hunger+=value
    def modify_energy(self, value=int):
        self.energy+=value

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes
print(f"Initial Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
whiskers.modify_hunger(-3)
#  - Increase energy by 2
whiskers.modify_energy(2)

# TODO: Print Whiskers' modified attributes
print(f"Modified Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")
