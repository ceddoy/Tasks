""" 
У вас есть список людей с возрастом и зарплатой, вот так:

[{"age": 18, "rate": 30}
{"age": 18, "rate": 15}
{"age": 50, "rate": 35}]

Напишите функцию, которая выводит среднюю зарплату по возрасту. В этом примере он должен выводить что-то вроде:

{"18": 22.5, "50": 35}

"""

import json


def load_file(fuction):
    """ Выгрузка из json в py."""
    def wrapper(file_name):
        with open(f"{file_name}.json", encoding="utf-8") as f:
            result = json.load(f)
            return fuction(result) # Результат возвращает в функцию averageSalaryByAge

    return wrapper


def average(dict_salaries):
    """ Расчет средней заработной платы. """
    for key, values in dict_salaries.items():
        dict_salaries[key] = sum(values) / len(values)
    return dict_salaries


@load_file
def averageSalaryByAge(data): # Передался список со вложенными словарями.
    resultAvrSalary = {} # Здесь будем хранить отфильтрованный результат данных.
    for data_dict in data:
        new_key = str(data_dict.get('age')) # При каждой итерации, будем присваивать переменной, ключ по возрастам.
        salary = data_dict.get('rate') # Аналогично, только тут будет значение (зарплата).
        """ Тут работаем уже с добавлением зарплат по ключу. """
        if new_key not in resultAvrSalary: # Здесь проверка на наличие возраста в результирующем словаре.
            resultAvrSalary[new_key] = [salary] # Если True, то создаем новый ключ со значением зарплаты
        else:                                   # списком, для хранения результата всех зарплат по возрасту.
            resultAvrSalary[new_key].append(salary) # Есть уже такой ключ есть, то просто добавляем значение к имеющемуся списку зарплат.
    return average(resultAvrSalary) # Результат возвращается уже с расчетом средней зарплаты по возврасту.

print(averageSalaryByAge("rate")) # -> load_file -> averageSalaryByAge
