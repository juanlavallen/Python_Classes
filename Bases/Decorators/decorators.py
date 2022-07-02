def decorator(func):
    def dec():
        print(f'Start the execution of the function: {func.__name__}')
        func()
        print(f'Terminate the execution of the function: {func.__name__}')

    return dec


@decorator
def show_name():
    print('Lionel Messi')


show_name()
