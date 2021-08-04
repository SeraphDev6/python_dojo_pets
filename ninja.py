from pet import *
class Ninja:
    def __init__(self,first_name,last_name,pets=[],treats={},pet_food=0):
        self.name=f"{first_name} {last_name}"
        self.pets=pets
        self.treats=treats
        self.pet_food=pet_food
        self.adopt_pet(Dog,"Fido")
    def adopt_pet(self,pet_type,name):
        new_pet = pet_type(name)
        self.pets.append(new_pet)
        print(f"{self.name} adopted a new {new_pet.type} named {new_pet.name}")
wes=Ninja("Wes","GG")
print(wes.pets)