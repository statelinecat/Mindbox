import unittest
import math
from mindbox_lib.shapes import Circle, Triangle, calculate_area


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), math.pi)

        circle = Circle(2.5)
        self.assertAlmostEqual(circle.area(), math.pi * 2.5 ** 2)

    def test_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

        triangle = Triangle(5, 5, 5)
        self.assertAlmostEqual(triangle.area(), 10.825317547305483)

    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)  # Не может существовать

        with self.assertRaises(ValueError):
            Triangle(0, 1, 1)  # Нулевая сторона

    def test_right_angled_triangle(self):
        self.assertTrue(Triangle(3, 4, 5).is_right_angled())
        self.assertTrue(Triangle(5, 12, 13).is_right_angled())
        self.assertFalse(Triangle(5, 5, 5).is_right_angled())

    def test_calculate_area_polymorphism(self):
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = [calculate_area(shape) for shape in shapes]
        self.assertAlmostEqual(areas[0], math.pi * 4)
        self.assertAlmostEqual(areas[1], 6.0)


if __name__ == "__main__":
    unittest.main()