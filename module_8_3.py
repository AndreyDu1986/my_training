class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.__set_vin_number(vin_number)
        self.__set_car_numbers(numbers)

    def __get_vin_number(self):
        return getattr(self, '_Car__vin_number')

    def __set_vin_number(self, value):
        if not isinstance(value, int):
            raise IncorrectVinNumber('Некорректный тип данных для win номера')
        if value < 1000000 or value > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для win номера')
        self.__vin_number = value

    def __get_car_numbers(self):
        return getattr(self, '_Car__numbers')

    def __set_car_numbers(self, value):
        if not isinstance(value, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(value) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        self.__numbers = value

    @staticmethod
    def __is_valid_vin(vin_number):
        try:
            if isinstance(vin_number, int):
                if 1000000 <= vin_number <= 9999999:
                    return True
                else:
                    raise IncorrectVinNumber('Неверный диапазон для win номера')
            else:
                raise IncorrectVinNumber('Некорректный тип данных для win номера')
        except IncorrectVinNumber as e:
            print(e.message)
            return False

    @staticmethod
    def __is_valid_numbers(numbers):
        try:
            if isinstance(numbers, str):
                if len(numbers) == 6:
                    return True
                else:
                    raise IncorrectCarNumbers('Неверная длина номера')
            else:
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        except IncorrectCarNumbers as e:
            print(e.message)
            return False

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')