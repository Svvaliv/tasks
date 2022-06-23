# Класс для нахождения расстояния между двумя точками

class Point():

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, func):
        if hasattr(func, 'x') and hasattr(func, 'y'):
            z = ((func.x - self.x) ** 2 + (func.y - self.y) ** 2) ** 0.5
            return z
        else:
            print('Передана не точка')


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)  # вернёт 5.0
print(d)
p1.get_distance(10)  # Распечатает "Передана не точка"
