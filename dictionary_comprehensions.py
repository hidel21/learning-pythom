def run():
#    my_dict = {}

    # for i in range (1,101):
    #     my_dict[i]= i**3


    # print(my_dict)

    my_dict = {i: i**3 for i in range(1,101) if 1 % 3 !=0}
    print(my_dict)

    #my_dict = {i : round(i**0.5,2) for i in  range(1,1001)}
        #print(my_dict)
        # """"Challenge numeros naturales con sus raices cuadradas
        # del 1 al 1000"""

if __name__ == '__main__':
    run()
