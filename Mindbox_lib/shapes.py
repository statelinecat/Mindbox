import math
from abc import ABC, abstractmethod
from typing import Union, Tuple


class Shape(ABC):
    """Абстрактный базовый класс для геометрических фигур."""

    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры."""
        pass

    @abstractmethod
    def is_right_angled(self) -> bool:
        """Проверяет, является ли фигура прямоугольной (если применимо)."""
        pass


class Circle(Shape):
    """Класс для представления круга."""

    def __init__(self, radius: float):
        """
        Инициализирует круг с заданным радиусом.

        Args:
            radius: Радиус круга (должен быть положительным).

        Raises:
            ValueError: Если радиус не положительный.
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        """Вычисляет площадь круга по формуле πr²."""
        return math.pi * self.radius ** 2

    def is_right_angled(self) -> bool:
        """Круг не может быть прямоугольным, всегда возвращает False."""
        return False


class Triangle(Shape):
    """Класс для представления треугольника."""

    def __init__(self, a: float, b: float, c: float):
        """
        Инициализирует треугольник с заданными сторонами.

        Args:
            a, b, c: Длины сторон треугольника (должны быть положительными).

        Raises:
            ValueError: Если стороны не положительные или не могут образовать треугольник.
        """
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Длины сторон должны быть положительными числами")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("С такими сторонами треугольник не существует")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """Вычисляет площадь треугольника по формуле Герона."""
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_angled(self, tolerance: float = 1e-6) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным.

        Args:
            tolerance: Допустимая погрешность при сравнении сторон.

        Returns:
            True, если треугольник прямоугольный, иначе False.
        """
        sides = sorted([self.a, self.b, self.c])
        # Проверяем теорему Пифагора с учетом погрешности
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < tolerance


def calculate_area(shape: Union[Circle, Triangle]) -> float:
    """
    Вычисляет площадь фигуры без знания её типа в compile-time.

    Args:
        shape: Объект фигуры (круг или треугольник).

    Returns:
        Площадь фигуры.
    """
    return shape.area()


# Пример использования:
if __name__ == "__main__":
    circle = Circle(5)
    print(f"Площадь круга: {calculate_area(circle)}")

    triangle = Triangle(3, 4, 5)
    print(f"Площадь треугольника: {calculate_area(triangle)}")
    print(f"Треугольник прямоугольный? {triangle.is_right_angled()}")