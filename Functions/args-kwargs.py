def add(*args):
    result = 0
    for n in args:
        result += n

    print(f'Result: {result}')


add(1, 1, 1, 1)  # 4
