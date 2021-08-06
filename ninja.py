from pet import *
from random import randint
class Ninja:
    def __init__(self,first_name,last_name,pets={},treats={},pet_food=0):
        self.name=f"{first_name} {last_name}"
        self.pets=pets
        self.treats=treats
        self.pet_food=pet_food
        self.adopt_pet(Dog,"Fido")
    def adopt_pet(self,pet_type,name):
        new_pet = pet_type(name)
        self.pets[name]=new_pet
        print(f"{self.name} adopted a new {new_pet.type} named {new_pet.name}")
    def Walk(self,pet_name):
        if pet_name in self.pets:
            self.pets[pet_name].play();
        else:
            print(f"{self.name} doesn't have a pet named {pet_name}")
    def feed(self,pet_name):
        if pet_name in self.pets:
            if self.pet_food>0:
                self.pet_food-=1
                self.pets[pet_name].eat();
            else:
                print(f"{self.name} doesn't have enough food. They should go get_food()!")
        else:
            print(f"{self.name} doesn't have a pet named {pet_name}")
    def get_food(self,quantity=1):
        self.pet_food+=quantity
        print(f"{self.name} got {quantity} more bags of pet food!")
    def bathe(self,pet_name):
        if pet_name in self.pets:
            self.pets[pet_name].noise();
        else:
            print(f"{self.name} doesn't have a pet named {pet_name}")
    def give_treat(self,pet_name,treat):
        if pet_name in self.pets:
            if treat in self.treats and self.treats[treat] > 0:
                print(f"{pet_name} enjoyed the {treat} so much they decide to do a trick!")
                self.pets[pet_name].do_trick(self.pets[pet_name].tricks[randint(0,len(self.pets[pet_name].tricks)-1)]);
            else:
                print(f"{self.name} doesn't have any {treat}s. They should go get_treats()!")
        else:
            print(f"{self.name} doesn't have a pet named {pet_name}")
    def get_treats(self,treat,quantity=1):
        if treat in self.treats:
            self.treats[treat]+= quantity
        else:
            self.treats[treat]=quantity
        print(f"{self.name} got {quantity} more {treat}(s)!")
    def teach_trick(self,pet_name,trick):
        if pet_name in self.pets:
            if trick in self.pets[pet_name].tricks:
                print(f"{pet_name} already knows how to {trick}!")
            else:
                self.pets[pet_name].tricks.append(trick)
                print(f"{pet_name} learned how to {trick}!")
        else:
            print(f"{self.name} doesn't have a pet named {pet_name}")



wes=Ninja("Wes","Giles")
wes.Walk("Odif")
wes.adopt_pet(Tyrannasaurus_Rex,"Fluffy")
wes.Walk("Fluffy")
wes.feed("Fluffy")
wes.get_food(100)
wes.feed("Fluffy")
wes.bathe("Fluffy")
wes.give_treat("Fluffy","bone")
wes.get_treats("bone",10)
wes.give_treat("Fluffy","bone")
wes.teach_trick("Fluffy","Chew bones")
wes.teach_trick("Fluffy","Eat civilian!")
wes.give_treat("Fluffy","bone")
wes.give_treat("Fluffy","bone")
wes.give_treat("Fluffy","bone")
wes.feed("Fluffy")