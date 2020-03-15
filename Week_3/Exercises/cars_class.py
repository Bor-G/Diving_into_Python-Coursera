import os
import csv

class CarBase:
    # индексы полей, которые соответствуют колонкам в исходном csv-файле
    i_ctype = 0
    i_brand = 1
    i_psc = 2
    i_pfn = 3
    i_b_whl = 4
    i_carr = 5
    i_ext = 6

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = "car"
    
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

    @classmethod
    def from_list(cls, row):
        return cls(
            row[cls.i_brand],
            row[cls.i_pfn],
            row[cls.i_carr],
            row[cls.i_psc],
        )        

class Truck(CarBase):
    car_type = "truck"

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.body_length, self.body_width, self.body_height = (float(c) for c in body_whl.split("x"))
        except ValueError:
            self.body_length, self.body_width, self.body_height = .0, .0, .0            
    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

    @classmethod
    def from_list(cls, row):
        return cls(
            row[cls.i_brand],
            row[cls.i_pfn],
            row[cls.i_carr],
            row[cls.i_b_whl],
        )        

class SpecMachine(CarBase):
    car_type = "spec_machine"

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    @classmethod
    def from_list(cls, row):
        return cls(
            row[cls.i_brand],
            row[cls.i_pfn],
            row[cls.i_carr],
            row[cls.i_ext],
        )

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок

        # объявим словарь, ключи которого - тип автомобиля (car_type),
        # а значения - класс, объект которого будем создавать
        car_dict = {car_class.car_type: car_class
                           for car_class in (Car, Truck, SpecMachine)}
        # обрабатываем csv-файл построчно
        for row in reader:
            try:
                # определяем тип автомобиля
                car_type = row[CarBase.i_ctype]
            except IndexError:
                # если не хватает колонок в csv - игнорируем строку
                continue
            try:
                # получаем класс, объект которого нужно создать
                # и добавить в итоговый список car_list
                car_class = car_dict[car_type]
            except KeyError:
                # если car_type не известен, просто игнорируем csv-строку
                continue
            try:
                # создаем и добавляем объект в car_list
                car_list.append(car_class.from_list(row))
            except (ValueError, IndexError):
                # если данные некорректны, то игнорируем их
                pass

    return car_list