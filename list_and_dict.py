def run():
    my_list= [1, "Hello", True, 123]
    my_dict= {'firstname':'facundo', 'lastname':'martoni'}

    super_list = [
        {'firstname':'Facundo', 'lastname':'martoni'},
        {'firstname':'Hidelberg', 'lastname':'Martinez'},
        {'firstname':'Jose', 'lastname':'Hernandez'},
        {'firstname':'Maria', 'lastname':'Mata'}
    ]

    super_dict = {
        'natural_nums':[1,2,3,4,5],
        'interger_nums':[-1,-2,0,1,2],
        'float_nums':[1.1,2.3,3.56]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


    if __name__ == '__main__':
        run()