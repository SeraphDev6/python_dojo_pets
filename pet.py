class Pet:
    def __init__(self,name,type,tricks=[],happiness=0,energy=100):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.happiness=happiness
        self.energy=energy
    def sleep(self):
        if(self.energy<100):
            self.energy=min(self.energy+25,100)
            print(f"{self.name} : Zzzzzz")
        else:
            print(f"{self.name} isn't tired. They want to play()!")
    def eat(self):
        if self.energy<100:
            self.energy=min(self.energy+5)
            self.happiness=min(self.happiness+10)
            print(f"{self.name} : Nom NOm NOM")
        else:
            print(f"{self.name} isn't hungry. They want to play()!")
    def play(self):
        if self.energy>10:
            self.happiness=min(self.happiness+5,100)
            self.energy-=10
            print(f"{self.name} had so much fun walking around the park!")
    def noise(self):
        pass
    def do_trick(self,trick):
        if trick in self.tricks:
            print(f"{self.name} did the {trick} trick!!")
            self.energy=max(self.energy-5,0)
        else:
            print(f"{self.name} looks at you confused..")
            print(f"They don't know how to {trick}...")
    def learn_trick(self,trick):
        if self.energy>20:
            self.energy-=20
            self.tricks.append(trick)
    def display_status(self):
        print(f"{self.name} is a {self.type}!")
        print(f"{self.name}'s happiness is {self.happiness}/100")
        print(f"{self.name}'s energy is {self.energy}/100")
        print(f"{self.name} knows these tricks:{self.tricks}")
class Dog(Pet):
    def __init__(self,name,tricks=[],happiness=0,energy=100):
        tricks.append("sit")
        tricks.append("wag tail")
        type="Dog"
        super().__init__(name,"Dog",tricks)
    def noise(self):
        print(f"{self.name} : BARK BARK!!")
class Tyrannasaurus_Rex(Pet):
    def __init__(self, name, tricks=[]):
        type="T-Rex"
        tricks.append("Chomp!")
        tricks.append("Chew bones")
        super().__init__(name, type, tricks)
    def noise(self):
        print(f"{self.name} : ROOOOOAAAAAAWWWWWWWRRRRRRRR!!!!!!!!")
    def play(self):
        print(f"{self.name} terrified everyone at the park! But they still had fun!")


if __name__ =="__main__":
    chompers=Tyrannasaurus_Rex("Chompers")
    print(chompers.name)
    chompers.noise()
    chompers.do_trick("Chew bones")