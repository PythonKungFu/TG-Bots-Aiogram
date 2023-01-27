print(dir())


from functions import get_double_number
import sys
from data import my_dict
from classes import *


print('Это исполняемый файл')


if __name__ == '__main__':
    print('Код ниже не выполнится, если этот файл будет импортируемым модулем в другой исполняемый файл')
    print(get_double_number(100))
    print(my_dict)
    MyClass()
    print(dir())
    print(sys.path)