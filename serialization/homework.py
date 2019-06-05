from constants import CARS_TYPES, CARS_PRODUCER, TOWNS

import random
import uuid
import json


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

class CustomerEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, object):
            return {'__name__': o.__class__.__name__,
                    '__data__': o.__dict__}


def from_json(obj):

    try:
        if obj.get('__name__') == 'Car':
            # print(obj.get('__data__'))
            obj = Car(price=obj.get('__data__').get('price'),
                        type=obj.get('__data__').get('type'),
                        producer=obj.get('__data__').get('producer'),
                        number=obj.get('__data__').get('number'),
                        milleage=obj.get('__data__').get('milleage'))


        if obj.get('__name__') == 'Garage':
            pass
            # print(obj.get('__data__'))
            # cars_lst = []
            # for cars in obj.get('__data__').get('cars'):
            #     car = Car(price=cars.get('__data__').get('price'),
            #                type=cars.get('__data__').get('type'),
            #                producer=cars.get('__data__').get('producer'),
            #                number=cars.get('__data__').get('number'),
            #                milleage=cars.get('__data__').get('milleage'))
            #     cars = cars.pop('__data__')
            #     cars_lst.append(car)
            #
            # obj.get('__data__').update({'cars': cars_lst})
            # print(obj.get('__data__').get('cars'))

        # if obj.get('__name__') == 'Cesar':
        #     print(obj.get('__data__'))
        return obj
    except:
        print('ZAEBALO')


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

    def __repr__(self):
        return f"name: {self.name}," \
            f"\nregister_id: {self.register_id}" \
            f"\ngarages: {self.garages}"

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
        return f"\n\tPrice: {self.price}, " \
            f"\n\tType: {self.type}, " \
            f"\n\tProducer: {self.producer}, " \
            f"\n\tNumber: {self.number}, " \
            f"\n\tMilleage: {self.milleage}"

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

    @staticmethod
    def from_json(obj):
        if obj.get('__name__') == 'Car':
            cars = Car(price=obj.get('__data__').get('price'),
                       type=obj.get('__data__').get('type'),
                       producer=obj.get('__data__').get('producer'),
                       number=obj.get('__data__').get('number'),
                       milleage=obj.get('__data__').get('milleage'))
            obj = cars
        return obj

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

    def __repr__(self):
        return f"\nTown: {self.town}" \
            f"\ncars: {self.cars}" \
            f"\nplaces: {self.places}" \
            f"\nonwer: {self.owner}"

    @staticmethod
    def generator(owner):
        return [Garage(owner) for _ in range(random.randrange(1, 3))]

    @staticmethod
    def from_json(obj):
        if obj.get('__name__') == 'Garage':

            garages = Garage(town=obj.get('__data__').get('town'),
                             cars=obj.get('__data__').get('cars'),
                             places=obj.get('__data__').get('places'),
                             owner=obj.get('__data__').get('owner'))
            obj = garages
        return obj

if __name__ == '__main__':

    """
    Init First and second Cesar. For each Cesar generate Garages and Cars
    """

    # print(tom.garages[0].cars)

    # print(json.dumps(tom.garages[0].cars, cls=CustomerEncoder, indent=4))


    # list_cars = []
    # for _ in range(1):
    #     list_cars.append(Car())
    #
    # garages_car = Garage(owner=234234234)
    # print(json.dumps(garages_car, cls=CustomerEncoder, indent=4))
    # garages = json.dumps(garages_car, cls=CustomerEncoder, indent=4)
    # print(json.loads(garages, object_hook=Garage.from_json))

    tom = Cesar(name='Tomas')
    # print(json.dumps(tom, cls=CustomerEncoder, indent=4))
    asd= json.dumps(tom, cls=CustomerEncoder, indent=4)

    print(json.loads(asd, object_hook= from_json))

