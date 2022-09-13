def cool_print_func():
    print('this was printed for the cool print function')
    return


def main():
    print('Welcome to COMP390')

    name1 = 'Joe'

    name_one = 'Mark'

    print(f'Hello, my name is {name1}')
    print(f'The answer is {2+3}')
    print(2+3)

    mystring = f'Hello, my name is {name1}'

    print(mystring)

    print(f'{cool_print_func()}')

    r_chat = name_one[2]
    print(r_chat)

    python_list = ['joe', 'mike', 'bob', 'james', 'mark']

    print(python_list.__len__())
    print(python_list.count('jill'))
    print(python_list.append('jill'))
    print(python_list.count('jill'))
    print(python_list)

    count = 0
    for name in python_list:
        #print(name, end=', ')
        print(f'name {count}: {name}')
        count += 1

    #for i in range(10):
    #    print(i)

    counter = 0
    while counter < 10:
        print(counter)
        counter += 2

    complex_python_list = [1, 'joe', 4.3, True, [2, 'vs.', [3.5, 'joe', 6.7], False]]

    print(f'this is index 2: {complex_python_list[2]}')

    print(complex_python_list)

    npc = {
        'name': 'joe',
        'hp': 100,
        'drop2': 'sword',
        'defence': 0.5,
        'drop1': 'sword'
    }

    npc['hp'] = 2000
    print(npc['hp'])

    for key, value in npc.items():
        print(f'{key}: {value}')

    #list comprehension (pythonic)
    search_result = [item for item in npc if npc[item] == 'sword']
    print(search_result)


if __name__ == '__main__':
    main()
