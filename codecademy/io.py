def greet_someone():
    name = input('What is your name?')
    hometown = input('And where are you from?')
    # displays str.format and formatted string literals
    print('Very nice to meet you, {}!'.format(name), f'from {hometown}!')
    # formatted string literals only
    print(f'Pleasure to meet you {name}, ', f'from {hometown.upper()}')
    # str.format only
    print('Gang! Gang! {} from {}'.format(name, hometown))


greet_someone()
