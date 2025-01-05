class Animal:
    def __init__(self, speed=1):
        self.live = True
        self.beak = True
        self.sound = None
        self._DEGREE_OF_DANGER = 0
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] - dz < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] -= dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        if self.sound is not None:
            print(self.sound)
        else:
            print("...")

class Bird(Animal):
    def lay_eggs(self):
        import random
        num_eggs = random.randint(1, 4)
        print(f"Here are {num_eggs} eggs for you.")

class AquaticAnimal(Animal):
    def dive_in(self, dz):
        self._cords[2] -= abs(dz) // 2
        self.speed /= 2

class PoisonousAnimal(Animal):
    def __init__(self, speed=1):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed=10):
        super().__init__(speed)
        super(PoisonousAnimal).__init__()
        super(AquaticAnimal).__init__()
        super(Bird).__init__()
        self.sound = "Click-click-click"

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()