def mybomb(count):
    print(f'Activating the bomb adn it will explode in {count} seconds')
    while count > 0:
        yield count
        count -= 1

    print('BAMM!')


for i in mybomb(10):
    print(f'---> {i}')
