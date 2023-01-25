print('Это основной файл main.py, его имя в процессе выполнения программы:', __name__)

# Variant 1
# from pack_1.file_11 import result
#
# print('result =', result)

# Variant 2
# from pack_2.pack_21.file_211 import r
# print('r =', r)

# Variant 3
from pack_2.pack_21.file_211 import r
print('r =', r)
