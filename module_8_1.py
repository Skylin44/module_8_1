def add_everything_up(a, b):
    try:
        if isinstance(a, float) and isinstance(b, int):
            return float("{:.3f}".format(a + b))
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            return str(a) + str(b)
    except TypeError:
        return str(a) + str(b)


 # Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
