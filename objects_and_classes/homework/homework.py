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

    def __init__(self, name, register_id, garages= []):
        self.name = name
        self.register_id = register_id
        self.garages = garages


    def hit_hat(self):
        total_price_cars = 0
        for x in self.garages:
            tom_garages_lst += len(x)
        return tom_garages_lst


    def garages_count(self):
        return len(self.garages)


    def сars_count(self):
        count_car = 0
        for x in self.garages:
            count_cat += len(x)
        return count_car


    def add_car(self):
        pass


    def display_all (self):
        print(self.name)
        print(self.register_id)
        print(self.garages)
        print("#####################")

class Car:

    def __init__(self):
        self.price = random.randrange(800,2000)
        self.type = random.choice(CARS_TYPES)
        self.producer = random.choice(CARS_PRODUCER)
        self.number = uuid.uuid4().hex
        self.milleage = random.randrange(1000)


    def __str__(self):
        return f"Price: {self.price}, Type: {self.type}, Producer: {self.producer}, Number: {self.number}, Milleage: {self.milleage}"


class Garage:

    def __init__(self, town, owner):
        self.town = town
        self.cars = [Car() for _ in range(random.randrange(5))]
        self.places = len(self.cars) + 5
        self.owner = owner


    def hit_hat(self):
        pass

    def __str__(self):
        return f"Cars in garages: {len(self.cars)}, Free places is: {self.places - len(self.cars)}, Owner is: {self.owner} "


if __name__ == '__main__':

    "Init First and second Cesar"

    Tom = Cesar(
        name='Tom',
        register_id= uuid.uuid4().hex,
        garages= [random.choice(TOWNS) for x in range(random.randrange(1,3))]
                )

    Jack = Cesar(
        name='Jack',
        register_id= uuid.uuid4().hex,
        garages= [random.choice(TOWNS) for x in range(random.randrange(1,3))]
        )

    "Init Garages and Cars for each Cesar"
    "---Tom's garages"

    tom_garages_lst = []
    for i in range(len(Tom.garages)):
        toms_garage = Garage(
            town= Tom.garages[i],
            owner= Tom.register_id
       )
        tom_garages_lst.append(toms_garage)


    "---Jack's garages"

    jack_garages_lst = []
    for i in range(len(Jack.garages)):
        jacks_garage = Garage(
            town= Jack.garages[i],
            owner= Jack.register_id
       )
        jack_garages_lst.append(jacks_garage)


    print(Tom.display_all())
    #print(Tom.garages_count())
    print('Kol garges is ' + str(Tom.garages_count()))
    print('Kol cars is ' + str(tom_garages_lst[0].cars[0].price))
    """
    for garage in :
        for car in garage:
        
    
    
    """


