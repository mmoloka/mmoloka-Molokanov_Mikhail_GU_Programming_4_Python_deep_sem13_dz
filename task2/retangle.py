from my_exceptions import NonNumericException, AboveZeroException

# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

class Rectangle:

    def __init__(self, length, width=None):
        self._length = length
        self._width = width or length

    def get_perimeter(self):
        return 2 * (self._length + self._width)

    def get_square(self):
        return self._length * self._width
    
    @property
    def get_length(self):
        return self._length
    
    @property
    def get_width(self):
        return self._width
    
    @get_length.setter
    def get_length(self, value):
        if not isinstance(value, (int, float)):
            raise NonNumericException(value)
        elif value > 0:
            self._length = value
        else:
            raise AboveZeroException(value)
        
    @get_width.setter
    def get_width(self, value):
        if not isinstance(value, (int, float)):
            raise NonNumericException(value)
        elif value > 0:
            self._width = value
        else:
            raise AboveZeroException(value)    


if __name__ == '__main__':
    r = Rectangle(5, 8)
    print(r.get_perimeter())
    # r.get_length = 'jhhvjh'
    # print(r.get_perimeter())
    # r.get_width = -84
    r.get_length = 0        