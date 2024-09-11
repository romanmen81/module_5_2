class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов объекта
        self.name = name  # Имя
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        # Метод для перехода на указанный этаж
        if new_floor < 1 or new_floor > self.number_of_floors:
            # Если этаж вне допустимых границ
            print("Такого этажа не существует")
        else:
            # Если этаж находится в допустимых границах, выводим все этажи до него
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        # Возвращаем количество этажей
        return self.number_of_floors

    def __str__(self):
        # Возвращаем строку с информацией о доме
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Создаем объекты класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Проверяем метод __str__
print(h1)
print(h2)

# Проверяем метод __len__
print(len(h1))
print(len(h2))