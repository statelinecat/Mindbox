from mindbox_lib.shapes import Circle, Triangle, calculate_area

circle = Circle(5)
print(circle.area())

triangle = Triangle(3, 4, 5)
print(triangle.area())
print(triangle.is_right_angled())

a = calculate_area(2, 5, 3, 8)
print(a)