def add(*args):
    result = 0
    for n in args:
        result += n

    print(f'Result: {result}')


add(1, 1, 1, 1)  # 4


def data(name, **kwargs):
    print(name, kwargs)


data('Juan', age=19, status=True)
