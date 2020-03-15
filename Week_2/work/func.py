def printer(*args):
    print(type(args))

    for argument in args:
        print(argument)

printer(1, 2, 3, 4, 5)

name_list = ['John', 'Bill', 'Amy']
printer(*name_list)

def printer(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print('{}: {}'.format(key, value))

printer (a=10, b=11)