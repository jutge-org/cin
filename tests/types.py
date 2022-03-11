from cin import *

x_int = read(int)
x_float = read(float)
x_str = read(str)
x_complex = read(complex)  # this is a mistake done un purpouse
x_empty = read()  # this is a mistake done un purpouse

print(x_int)
print(x_float)
print(x_str)
print(x_complex)
print(x_empty)

reveal_type(read(int))
reveal_type(read(float))
reveal_type(read(str))

reveal_type(scan(int))
reveal_type(scan(float))
reveal_type(scan(str))
