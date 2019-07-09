import sys
from time import *
def GPS ():
    global gen_0
    global S_SR
    global A_SR
    global J_SR
    global seniles
    global adults
    global juviniles
    global A_BR
    print ('Please select a option from the menu below \n\n 1-|Input generation values\n 2-|Display generation values\n 3-|Run simulator\n 4-|Export data\n 5-|Quit ')
    GM = input()
    if GM == '1' :
        gen_0 = int(input ('how many generations do you want to run '))
        S_SR = float(input ('pick the senile survival rate (between 1 and 0): '))
        A_SR =  float(input ('pick the adult survival rate (between 1 and 0): '))
        J_SR = float(input('pick the juvinile survival rate (between 1 and 0): '))
        seniles = float(input ('how many seniles do you want to have '))
        adults = float(input ('how many adults do you want to have '))
        juviniles = float(input ('how many juviniles do you want to have '))
        A_BR =  float(input ('pick the adult birth rate '))
        print()
        GPS()
    elif GM == '2':
        print (gen_0)
        print ('the number of generations runing is: ', gen_0 ,)
        print ('the initial population for the adults is: ', adults,)
        print ('the initial population for the seniles is: ', seniles,)
        print ('the initial population for the juviniles is: ', juviniles,)
        print ('the birth rate for adults is: ',A_BR,)
        print ('the survival rate for the adults is: ',A_SR,)
        print ('the survival rate for the juviniles is: ',J_SR,)
        print ('the survival rate for the seniles is: ',S_SR,)
        print()
        GPS()
    elif GM == '3':
        gens = 0
        for i in range (gen_0):
            '''print('        ________________________________')
            print('        |           |        |         |')
            print('        | juviniles | adults | seniles |')
            print('gen: ',gens,'|  ',juviniles,'   | ',adults,' |  ',seniles,' |')
            print('gen: ',gens,'|  ',juviniles,'   | ',adults,' |  ',seniles,' |')
            print('gen: ',gens,'|  ',juviniles,'   | ',adults,' |  ',seniles,' |')
            print('gen: ',gens,'|  ',juviniles,'   | ',adults,' |  ',seniles,' |')
            print('gen: ',gens,'|  ',juviniles,'   | ',adults,' |  ',seniles,' |')
            print('        |___________|________|_________|')'''
            print('gen:',gens)
            print()
            print('seniles:',seniles)
            print('adults:',adults)
            print('juviniles:',juviniles)
            S_storage = seniles
            A_storage = adults
            J_storage = juviniles

            J_storage = adults*A_BR
            A_storage = juviniles*J_SR
            S_storage = adults*A_SR
            S_storage = S_storage+seniles*S_SR

            seniles = S_storage
            adults = A_storage
            juviniles = J_storage

            gens = gens + 1
            sleep(1)
            print()
        print()
        GPS()
    elif GM == '4':
        print()
        GPS()
    elif GM == '5':
        exit()
GPS()
