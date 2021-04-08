def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Cesar', 'lastname': 'Hera'}
    
    super_list = [
    {'firstname': 'Cesar', 'lastname': 'Hera'},
    {'firstname': 'Facundo', 'lastname': 'García'},
    {'firstname': 'Isaias', 'lastname': 'Hernandez'}
    ]

    super_dict = {
    'natural_nums': [1, 2, 3, 4, 5, 6],
    'integer_nums': [-1, -2, 0, 1, 2],
    'floating_nums': [0.1, 0.4, 3.5, -3.1]
    }


    # for key, value in super_dict.items(): 
    #     print(key, '-', value)

    for values in super_list:
        for key, value in values.items():
            print(key, '-', value)

if __name__ == '__main__':
    run()