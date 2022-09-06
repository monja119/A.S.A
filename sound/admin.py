import os
print(os.__file__)

try:
    a = 1+'v'
except TypeError as tp:
    print(tp)
