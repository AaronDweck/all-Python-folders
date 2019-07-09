
print("aarons car park\n")

carReg = input("please enter the last three digits of yuor car registration")                        
print("please insert the full price for a ticket\n")

totalcash  = 0

while totalcash < 8:
    coins = int(input("enter pound coins: "))
    totalcash = totalcash + coins
    print("total cash paid so far:",totalcash)

if totalcash > 8:
    print("change due",totalcash-8)
else:
    print("here is your ticket. thank you for using this machine.\n")
#creat the parking ticket

if totalcash<10:
    padding="                      *"
else:
    padding="                     *"

print("printing your ticket...")
print()
print()
print("*******************************************")
print("*            parking ticket               *")
print("*                                         *")
print("*      fee paid £",totalcash,padding)
print("*                                         *")
print("*     car registration:",carReg,"              *")
print("*******************************************")
print()
print()
