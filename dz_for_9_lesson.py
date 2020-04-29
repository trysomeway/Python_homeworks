class Car:
    def __init__(self, speed=180, weight=1000, praise=10000, sound='Pi'):
        self.speed = speed
        self.weight = weight
        self.praise = praise
        self.sound = sound

    def compared_with_gepard(self):
        if self.speed > 100:
            print("It faster than gepard") 
        else:
            print("Gepard is faster than it")

    def it_sound(self, your_name="Dude"):
        print(f'{self.sound}, {your_name}!')

    def expensive(self, how_much_is_expensive_for_you=100000):
        if self.praise > how_much_is_expensive_for_you:
            print("It cost expensive!")
        else:
            print(f"It cost less than {how_much_is_expensive_for_you}$...")
    

class Car_amphibe(Car):
    def __init__(self, speed=150, weight=1200, praise=100000, sound='Bul'):
        self.speed = speed
        self.weight = weight
        self.praise = praise
        self.sound = sound


class Airplane(Car):
    def __init__(self, speed=900, weight=2000, praise=1000000, sound='Yyy'):
        self.speed = speed
        self.weight = weight
        self.praise = praise
        self.sound = sound


class Ship(Car):
    def __init__(self, speed=30, weight=10000, praise=500000, sound='Pam'):
        self.speed = speed
        self.weight = weight
        self.praise = praise
        self.sound = sound


# car = Car()
# car.it_sound("Dude")
# car.expensive(50)
# car.compared_with_gepard()

# amphibe = Car_amphibe()
# amphibe.it_sound()
# amphibe.expensive(100)
# amphibe.compared_with_gepard()
