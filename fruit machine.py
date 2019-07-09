from random import *
from time import *

reel = ['lemon','lemon','lemon','lemon','lemon','lemon','lemon','lemon','lemon','lemon','orange','orange','orange','orange','orange','orange','orange','cherry','cherry','cherry','cherry','cherry','cherry','bell','bell','bell','bell','bell','bell','bell','bell','bar','bar','bar','bar','bar','bar','bar','bar2','bar2','bar2','bar2','bar2','bar2','bar2','bar3','bar3','bar3','bar3','bar3']


goes = 0
print('welcome to my slot machine')
sleep(1.5)
print('it is £5 each turn')
sleep(1.5)
money = int(input('how much money do you want to play with ? '))
while money>0:
    goes = goes+1
    money = money-5
    print(goes)

    reel1 = choice(reel)
    reel2 = choice(reel)
    reel3 = choice(reel)
    reel4 = choice(reel)


    print (reel1+' '+reel2+' '+reel3+' '+reel4)
    sleep(0.)
   # def board():
    

    if (reel1=='lemon' and reel1==reel2 and reel1==reel3) or (reel1=='lemon' and reel1==reel3 and reel1==reel4) or (reel1=='lemon' and reel1==reel2 and reel1==reel4) or (reel2=='lemon' and reel2==reel3 and reel2==reel4):
                print('you got a')
                print('£ 2.50 jackpot')
                money = money+2.50
                print('£',money)
                sleep(2)
                leaving = input('do you want to leave [Y|N]? ')
                if leaving == 'y':
                    print('you left with: £',money)
                    sleep(2)
                    break
    elif reel1=='lemon' and reel1==reel2 and reel1==reel3 and reel1==reel4:
                print('you got a')
                print('£5 jackpot')
                money = money+5
                print('£',money)
                sleep(2)
                leaving = input('do you want to leave [Y|N]? ')
                if leaving == 'y':
                    print('you left with: £',money)
                    sleep(2)
                    break
    elif (reel1=='orange' and reel1==reel2 and reel1==reel3) or (reel1=='orange' and reel1==reel3 and reel1==reel4) or (reel1=='orange' and reel1==reel2 and reel1==reel4) or (reel2=='orange' and reel2==reel3 and reel2==reel4):
                print('you got a')
                print('£ 7.50 jackpot')
                money = money+7.50
                print('£',money)
                sleep(2)
                leaving = input('do you want to leave [Y|N]? ')
                if leaving == 'y':
                    print('you left with: £',money)
                    sleep(2)
                    break
    elif reel1=='orange' and reel1==reel2 and reel1==reel3 and reel1==reel4:
                print('you got a')
                print('£10 jackpot')
                money = money+10
                print('£',money)
                sleep(2)
                leaving = input('do you want to leave [Y|N]? ')
                if leaving == 'y':
                    print('you left with: £',money)
                    sleep(2)
                    break
    elif (reel1=='cherry' and reel1==reel2 and reel1==reel3) or (reel1=='cherry' and reel1==reel3 and reel1==reel4) or (reel1=='cherry' and reel1==reel2 and reel1==reel4) or (reel2=='cherry' and reel2==reel3 and reel2==reel4):
                print('you got a')
                print('£ 13.50 jackpot')
                money = money+13.50
                print('£',money)
                sleep(2)
                leaving = input('do you want to leave [Y|N]? ')
                if leaving == 'y':
                    print('you left with: £',money)
                    sleep(2)
                    break
    elif reel1=='cherry' and reel1==reel2 and reel1==reel3 and reel1==reel4:
                print('you got a')
                print('£15 jackpot')
                money = money+15
                print('£',money)
                sleep(2)
                leaving = input('do you want to leave [Y|N]? ')
                if leaving == 'y':
                    print('you left with: £',money)
                    sleep(2)
                    break
    elif (reel1=='bell' and reel1==reel2 and reel1==reel3) or (reel1=='bell' and reel1==reel3 and reel1==reel4) or (reel1=='bell' and reel1==reel2 and reel1==reel4) or (reel2=='bell' and reel2==reel3 and reel2==reel4):
            print('you got a')
            print('£ 17.50 jackpot')
            money = money+17.50
            print('£',money)
            sleep(2)
            leaving = input('do you want to leave [Y|N]? ')
            if leaving == 'y':
                print('you left with: £',money)
                sleep(2)
                break
    elif reel1=='bell' and reel1==reel2 and reel1==reel3 and reel1==reel4:
            print('you got a')
            print('£20 jackpot')
            money = money+20
            print('£',money)
            sleep(2)
            leaving = input('do you want to leave [Y|N]? ')
            if leaving == 'y':
                print('you left with: £',money)
                sleep(2)
                break
    elif (reel1=='bar' and reel1==reel2 and reel1==reel3) or (reel1=='bar' and reel1==reel3 and reel1==reel4) or (reel1=='bar' and reel1==reel2 and reel1==reel4) or (reel2=='bar' and reel2==reel3 and reel2==reel4):
            print('you got a')
            print('£ 22.50 jackpot')
            money = money+22.50
            print('£',money)
            sleep(2)
            leaving = input('do you want to leave [Y|N]? ')
            if leaving == 'y':
                print('you left with: £',money)
                sleep(2)
                break
    elif reel1=='bar' and reel1==reel2 and reel1==reel3 and reel1==reel4:
            print('you got a')
            print('£25 jackpot')
            money = money+25
            print('£',money)
            sleep(2)
            leaving = input('do you want to leave [Y|N]? ')
            if leaving == 'y':
                print('you left with: £',money)
                sleep(2)
                break
    elif (reel1=='bar2' and reel1==reel2 and reel1==reel3) or (reel1=='bar2' and reel1==reel3 and reel1==reel4) or (reel1=='bar2' and reel1==reel2 and reel1==reel4) or (reel2=='bar2' and reel2==reel3 and reel2==reel4):
            print('you got a')
            print('£ 27.50 jackpot')
            money = money+27.50
            print('£',money)
            sleep(2)
            leaving = input('do you want to leave [Y|N]? ')
            if leaving == 'y':
                print('you left with: £',money)
                sleep(2)
                break
    elif reel1=='bar2' and reel1==reel2 and reel1==reel3 and reel1==reel4:
            print('you got a')
            print('£30 jackpot')
            money = money+30
            print('£',money)
            sleep(2)
            leaving = input('do you want to leave [Y|N]? ')
            if leaving == 'y':
                print('you left with: £',money)
                sleep(2)
                break
    elif (reel1=='bar3' and reel1==reel2 and reel1==reel3) or (reel1=='bar3' and reel1==reel3 and reel1==reel4) or (reel1=='bar3' and reel1==reel2 and reel1==reel4) or (reel2=='bar3' and reel2==reel3 and reel2==reel4):
            print('you got a')
            print('£ 32.50 jackpot')
            money = money+32.50
            print('£',money)
            sleep(2)
            leaving = input('do you want to leave [Y|N]? ')
            if leaving == 'y':
                print('you left with: £',money)
                sleep(2)
                break
    elif reel1=='bar3' and reel1==reel2 and reel1==reel3 and reel1==reel4:
            print('you got a')
            print('£35 jackpot')
            money = money+35
            print('£',money)
            sleep(2)
            leaving = input('do you want to leave [Y|N]? ')
            if leaving == 'y':
                print('you left with: £',money)
                sleep(2)
                break
    else:
            print('you lose')
            print('£',money)
            sleep(2)
            leaving = input('do you want to leave [Y|N]? ')
            if leaving == 'y':
                print('you left with: £',money)
                sleep(2)
                break
            
input('press enter to leave')
exit()
