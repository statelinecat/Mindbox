# Mindbox
 Mindbox test

Библиотека для вычисления площадей геометрических фигур.

## Установка

```bash
pip install -e .
```

## Использование

```python
from mindbox_lib.shapes import Circle, Triangle

circle = Circle(5)
print(circle.area())

triangle = Triangle(3, 4, 5)
print(triangle.area())
print(triangle.is_right_angled())
```

## Тестирование

```bash
python -m unittest discover tests
```
