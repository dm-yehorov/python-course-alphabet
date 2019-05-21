from constants import CARS_TYPES, CARS_PRODUCER, TOWNS

import random
import uuid


"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.
Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.
    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.
    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID
Гараж має наступні характеристики:
    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.
    Повинен мати реалізованими наступні методи
    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі
Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.
    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.
    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""


class Cesar:

    def __init__(self, name, garages=None):
        self.name = name
        self.register_id = uuid.uuid4().hex
        self.garages = garages or Garage.generator(self.register_id)

    def hit_hat(self):
        total_price_cars = 0
        for x in self.garages:
            for y in range(len(x.cars)):
                total_price_cars += x.cars[y].price
        return total_price_cars

    def garages_count(self):
        return len(self.garages)

    def сars_count(self):
        count_car = 0
        for x in self.garages:
            count_car += len(x.cars)
        return count_car

    def add_car(self, garag=None):
       self.garag=garag
       free_places_lst=[i.free_places() for i in self.garages]
       if garag is None:
            if max(free_places_lst) > 0:
                self.garages[free_places_lst.index(max(free_places_lst))].cars.append(Car())
            else:
                print('Not free places in any garages')
       else:
           self.garag.add()


    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

class Car:

    def __init__(self, price = None, type = None, producer = None, number = None, milleage = None):
        self.price = price or random.randrange(800,2000)
        self.type = type or random.choice(CARS_TYPES)
        self.producer = producer or random.choice(CARS_PRODUCER)
        self.number = number or uuid.uuid4().hex
        self.milleage = milleage or random.randrange(1000)

    def chg_num(self):
        self.number = uuid.uuid4().hex

    def __repr__(self):
        return f"Price: {self.price}, " \
            f"Type: {self.type}, " \
            f"Producer: {self.producer}, " \
            f"Number: {self.number}, " \
            f"Milleage: {self.milleage}"

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __gt__(self, other):
        return self.price > other.price

    @staticmethod
    def generator():
        return [Car() for _ in range(random.randrange(1,5))]

class Garage:

    def __init__(self, owner=None, cars=None, places=None, town=None):
        self.town = town or random.choice(TOWNS)
        self.cars = cars or Car.generator()
        self.places = places or len(self.cars) + random.randrange(5)
        self.owner = owner

    def add(self):
        if self.places - len(self.cars) > 0:
            self.cars.append(Car())
        else:
            print('I dont have free places')

    def remove(self):
        if len(self.cars) > 0:
            self.cars.pop(random.randrange(len(self.cars)))

    def hit_hat(self):
        total_price_cars = 0
        for i in range(len(self.cars)):
            total_price_cars += self.cars[i].price
        return total_price_cars

    def free_places(self):
        return self.places - len(self.cars)

    @staticmethod
    def generator(owner):
        return [Garage(owner) for _ in range(random.randrange(1, 3))]

if __name__ == '__main__':

    """
    Init First and second Cesar. For each Cesar generate Garages and Cars
    """
    Tom = Cesar(name='Tom')
    Jack = Cesar(name='Jack')

    " Lets show number of garages and cars "

    print(f'Count Garages for Tom: {Tom.garages_count()}')
    print(f'Count Garages for Jack: {Jack.garages_count()}')
    print(f'Count Cars for Tom: {Tom.сars_count()}')
    print(f'Count Cars for Jack: {Jack.сars_count()}')

    "Hit_hat fo each Cesar"
    print(f'Sum money all cars for Tom: {Tom.hit_hat()}')
    print(f'Sum money all cars for Jack: {Jack.hit_hat()}')
    print(f'Tom.hit_hat() == Jack.hit_hat() is: {Tom.hit_hat() == Jack.hit_hat()}')

    "Hit_hat fo each Garase for Cesar"
    "Tom's garages"
    for i in range(Tom.garages_count()):
        print(f'Sum money all cars in each Garages for Tom: {Tom.garages[i].hit_hat()}')

    "Jack's garages"
    for i in range(Jack.garages_count()):
        print(f'Sum money all cars in each Garages for Jack: {Jack.garages[i].hit_hat()}')

    "Logs car in each Garages for Tom"
    print("For Toms")
    for i in Tom.garages:
        for j in i.cars:
            print(j)
    "Logs car in each Garages for Jack"
    print("For Jack")
    for i in Jack.garages:
        for j in i.cars:
            print(j)

    print('Tom.garages[0].cars[0] > Jack.garages[0].cars[0] is ', Tom.garages[0].cars[0] > Jack.garages[0].cars[0])

    print("Add Cars to Tom.Garages")
    for i in Tom.garages:
        for j in i.cars:
            print(j)

    print("Add Cars to Jack.Garages")
    Jack.add_car()
    for i in Jack.garages:
        for j in i.cars:
            print(j)

    print("Change number for random car in random for Tom")
    print(Tom.garages[0].cars[0])
    Tom.garages[0].cars[0].chg_num()

    print("Change number for random car in random for Jack")
    print(Jack.garages[0].cars[0])
    Jack.garages[0].cars[0].chg_num()

    print("Remove Cars to Tom.Garages")
    for i in Tom.garages:
        if len(i.cars) > 0:
            i.cars.pop(random.randrange(len(i.cars)))
            break
    for i in Tom.garages:
        for j in i.cars:
            print(j)

    print("Remove Cars to Jack.Garages")
    for i in Jack.garages:
        if len(i.cars) > 0:
            i.cars.pop(random.randrange(len(i.cars)))
            break
    for i in Jack.garages:
        for j in i.cars:
            print(j)

    print('Cesar Add Cars in each garages')
    Tom.add_car(garag= Tom.garages[0])
    for i in Tom.garages:
        for j in i.cars:
            print(j)

