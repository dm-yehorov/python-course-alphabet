from constants import *
from typing import List

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

    def __init__(self, name):
        self.name = name
        self.register_id = uuid.uuid4().hex
        self.garages = [Garage(owner= self.register_id) for _ in range(random.randrange(1,3))]


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


    def add_car(self):
       free_places_lst = [i.free_places() for i in self.garages ]
       if max(free_places_lst) > 0:
            self.garages[free_places_lst.index(max(free_places_lst))].cars.append(Car())
       else:
            return ('Not free places in any garages')


class Car:

    def __init__(self):
        self.price = random.randrange(800,2000)
        self.type = random.choice(CARS_TYPES)
        self.producer = random.choice(CARS_PRODUCER)
        self.number = uuid.uuid4().hex
        self.milleage = random.randrange(1000)


    def chg_num(self):
        self.number = uuid.uuid4().hex


    def __str__(self):
        return f"Price: {self.price}, Type: {self.type}, Producer: {self.producer}, Number: {self.number}, Milleage: {self.milleage}"


class Garage:

    def __init__(self, owner):
        self.town = random.choice(TOWNS)
        self.cars = [Car() for _ in range(random.randrange(5))]
        self.places = len(self.cars) + random.randrange(5)
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


if __name__ == '__main__':

    """
    Init First and second Cesar. For each Cesar generate Garages and Cars

    """
    Tom = Cesar(name='Tom')
    Jack = Cesar(name='Jack')

    " Lets show number of garages and cars "

    print('Count Garages for Tom ' + str(Tom.garages_count()))
    print('Count Garages for Jack ' + str(Jack.garages_count()))
    print('Count Cars for Tom ' + str(Tom.сars_count()))
    print('Count Cars for Jack ' + str(Jack.сars_count()))

    "Hit_hat fo each Cesar"

    print('Sum money all cars for Tom ' + str(Tom.hit_hat()))
    print('Sum money all cars for Jack ' + str(Jack.hit_hat()))

    "Hit_hat fo each Garase for Cesar"
    "Tom's garages"
    for i in range(Tom.garages_count()):
        print('Sum money all cars in each Garages for Tom ' + str(Tom.garages[i].hit_hat()))

    "Jack's garages"
    for i in range(Jack.garages_count()):
        print('Sum money all cars in each Garages for Jack ' + str(Jack.garages[i].hit_hat()))

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

    print("Add Cars to Tom.Garages")
    Tom.add_car()
    for i in Tom.garages:
        for j in i.cars:
            print(j)

    print("Add Cars to Jack.Garages")
    Jack.add_car()
    for i in Jack.garages:
        for j in i.cars:
            print(j)

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

    print("Change number for random car in random for Tom")
    print(Tom.garages[0].cars[0])
    Tom.garages[0].cars[0].chg_num()
