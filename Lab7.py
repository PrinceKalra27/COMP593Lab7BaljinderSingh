

def main():

    info_keys = {
        'name' : 'Baljinder Singh',
        'student_id' : '10266917',
        'pizza_toppings' : [
            'cheese',
            'chicken',
            'paneer',
        ],
        'movies' : [
            {'title' :'Harry Potter',
            'genre' : 'Magic',
            },
            {'title' : 'Ardas',
            'genre' : 'Drama/religious',
            }
        ]
    }

    new_movie = {'title' : 'The Karate Kid',
            'genre' : 'MartialArts/Inspirational',
            }
    info_keys['movies'].append(new_movie)

    new_toppings = ('spinach','pineapple')
    add_new_toppings(info_keys, new_toppings)

    #for b in info_keys['movies']:
    #    print(b['title'])
    print_statement1(info_keys)
    print_statement2(info_keys)
    print_statement3(info_keys)
    print_statement4(info_keys)

    pass

def add_new_toppings(info, tpngs):

    for t in tpngs:
        info['pizza_toppings'].append(t)
        info['pizza_toppings'].sort()

def print_statement1(info):
    
    print('Hi Joe, my name is', info['name'],'and my student ID is', info['student_id'] , end='.' '\n')

def print_statement2(info):

    print('My ideal pizza has', end=' ')

    for i,p in enumerate(info['pizza_toppings']):

        if i < len(info['pizza_toppings']) - 1:
            print(p,end=', ')
        else:
            print(p, end='.')

    print(' ')

def print_statement3(info):
    
    line3 = 'I like to watch '

    for i,g in enumerate(info['movies']):

        if i < len(info['movies']) - 1:
            line3 += g['genre'] + ', '
        else:
            line3 += g['genre'] + ' movies.'

    print(line3)
    

def print_statement4(info):

    line4 = 'Some of my favourites are'

    for i,tm in enumerate(info['movies']):
        line4 += tm['title']
        if i < len(info['movies']) - 1:
            line4 += ', '
        else:
            line4 += '!'

    print(line4)

    





main()