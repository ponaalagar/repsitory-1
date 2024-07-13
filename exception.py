class ve(Exception):
    pass
a=int(input())
try:
    if a<0:
        raise ve('the value must not be lower that zero')
except ve as v:
    print(v)
except TypeError:
    print('valuedwoefij')
