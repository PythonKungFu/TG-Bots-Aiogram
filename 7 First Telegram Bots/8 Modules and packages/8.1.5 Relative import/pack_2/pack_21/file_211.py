print('Это файл', __name__)


from ..file_21 import another_some_func
from ...file_0 import some_var


b: int = 4242
some_dict: dict[int, str] = {1: 'A',
                             2: 'B',
                             3: 'C'}

r = another_some_func(some_var)
