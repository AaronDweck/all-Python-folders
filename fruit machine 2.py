

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
    print(goes)#
    

    reel1 = choice(reel)
    reel2 = choice(reel)
    reel3 = choice(reel)
    reel4 = choice(reel)    
    keep = reel1

    print (reel1+' '+reel2+' '+reel3+' '+reel4)
    pr = [reel1,reel2,reel3,reel4]
    
    
    sleep(1) 
def people_leaving():
    leaving = input('do you want to leave [Y|N]? ')
    if leaving == 'y':
        print('you left with: £',money)
        quit
        
    
        if(reel1==reel2 and reel1==reel3) or (reel1==reel3 and reel1==reel4) or (reel2==reel3 and reel2==reel4):
            if (reel1=='lemon') or (reel2 == 'lemon'):
                print('you got a\n£ 2.50 jackpot')
                money = money+2.50
                print('£',money)
                sleep(2)
                people_leaving()
            elif (reel1=='orange') or (reel2 == 'orange'):
                print('you got a\n£ 7.50 jackpot')
                money = money+7.50
                print('£',money)
                sleep(2)
                people_leaving()
            elif (reel1=='cherry') or (reel2 == 'cherry'):
                print('you got a\n£ 13.50 jackpot')
                money = money+13.50
                print('£',money)
                sleep(2)
                people_leaving()
            elif (reel1=='bell') or (reel2 == 'bell'):
                print('you got a\n£ 17.50 jackpot')
                money = money+17.50
                print('£',money)
                sleep(2)
                people_leaving()
            elif (reel1=='bar') or (reel2 == 'bar'):
                print('you got a\n£ 22.50 jackpot')
                money = money+22.50
                print('£',money)
                sleep(2)
                people_leaving()
            elif (reel1=='bar2') or (reel2 == 'bar2'):
                print('you got a\n£ 27.50 jackpot')
                money = money+27.50
                print('£',money)
                sleep(2)
                people_leaving()
            elif (reel1=='bar3') or (reel2 == 'bar3'):
                print('you got a\n£ 32.50 jackpot')
                money = money+32.50
                print('£',money)
                sleep(2)
                people_leaving()
        elif reel1==reel2 and reel1==reel3 and reel1==reel4:
            if reel1=='lemon':
                print('you got a\n£ 5 jackpot')
                money = money+5
                print('£ ',money)
                sleep(2)
                people_leaving()
            elif reel1=='orange':
                print('you got a\n£ 10 jackpot')
                money = money+10
                print('£ ',money)
                sleep(2)
                people_leaving()
            elif reel1=='cherry':
                print('you got a\n£ 15 jackpot')
                money = money+15
                print('£ ',money)
                sleep(2)
                people_leaving()
            elif reel1=='bell':
                print('you got a\n£ 20 jackpot')
                money = money+20
                print('£ ',money)
                sleep(2)
                people_leaving()
            elif reel1=='bar':
                print('you got a\n£ 25 jackpot')
                money = money+25
                print('£ ',money)
                sleep(2)
                people_leaving()
            elif reel1=='bar2':
                print('you got a\n£ 30 jackpot')
                money = money+30
                print('£ ',money)
                sleep(2)
                people_leaving()
            elif reel1=='bar3':
                print('you got a\n£ 35 jackpot')
                money = money+35
                print('£ ',money)
                sleep(2)
                people_leaving()
    

        else:
            print('you lose')
            print('£',money)
            sleep(2)
            leaving = input('do you want to leave [Y|N]? ')
            if leaving == 'y':
                print('you left with: £',money)
                sleep(2)
                quit
            
input('press enter to leave')
exit()

