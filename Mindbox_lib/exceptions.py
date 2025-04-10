class GeometryError(Exception):
    """Базовое исключение для всех ошибок библиотеки геометрии"""
    pass


class NegativeValueError(GeometryError):
    """Ошибка при передаче отрицательного значения"""
    def __init__(self, value_name: str, value: float):
        self.value_name = value_name
        self.value = value
        super().__init__(f"{value_name} не может быть отрицательным, получено: {value}")


class TriangleExistError(GeometryError):
    """Ошибка, когда треугольник не может существовать с заданными сторонами"""
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(
            f"Треугольник со сторонами {a}, {b}, {c} не может существовать. "
            "Сумма любых двух сторон должна быть больше третьей."
        )