# Define the base class 'superHero'
class superHero():
    def __init__(self, name, description, hasCap, ability, health):
        # Initialize the superhero's properties
        self.name = name
        self.description = description
        self.hasCap = hasCap  # Boolean: Does the hero wear a cape?
        self.ability = ability  # The superhero's special power
        self.__health = health  # Private attribute: health is encapsulated

    # Introduce the superhero
    def introduce(self):
        print(f"I am {self.name}, {self.description}. My super power is {self.ability}.")

    # Simulate an attack on a target
    def attack(self, target):
        print(f"{self.name} attacks {target} using {self.ability}!")

    # Apply damage to the superhero and reduce health
    def take_damage(self, amount):
        self.__health -= amount
        if self.__health > 0:
            print(f"{self.name} took {amount} damage. Health is now {self.__health}.")
        else:
            self.__health = 0
            print(f"{self.name} has been defeated.")


# Define the Villain class inheriting from superHero
class Villain(superHero):
    def __init__(self, name, description, hasCap, ability, evil_plan, health):
        # Initialize parent class (superHero) attributes
        super().__init__(name, description, hasCap, ability, health)
        self.evil_plan = evil_plan  # Extra property unique to villains

        self.__villain_health = health 

    # Villain reveals their evil plan
    def revel_plan(self):
        print(f"I am {self.name} and I plan to {self.evil_plan}.")

    # Override: Apply damage to the villain and reduce health
    def take_damage(self, amount):
        self.__villain_health -= amount
        if self.__villain_health > 0:
            print(f"{self.name} took {amount} damage. Health is now {self.__villain_health}.")
        else:
            self.__villain_health = 0
            print(f"{self.name} has been defeated.")

    def get_health(self):  # Getter for villain's health
        return self.__villain_health


# Create two superhero instances
superHero1 = superHero("Iron Man", "Tony Stark", False, "Rich", 100)
superHero2 = superHero("Thor", "The God of Thunder", True, "Lightning", 100)

# Introduce Thor
superHero.introduce(superHero2)  # Calls introduce on superHero2

# Simulate Iron Man taking damage twice
superHero1.take_damage(30)  # Health reduces by 30
superHero1.take_damage(30)  # Health reduces by another 30

# Create a Villain instance
villain1 = Villain(
    "Thanos", 
    "Conquerer of realms", 
    False, 
    "Infinity Stones", 
    "Wipe out half of the population in the universe", 
    100
)

# Villain takes damage
villain1.take_damage(50)  # Health reduces by 50
