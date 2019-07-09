
operation = ""

while operation != "quit":
    num1 = int(input("enter your first number:"))
    num2 = int(input("enter your second number:"))

    operation=input("ok,so what do you want to do wht these numbers?:")

    if operation == "add":
        answer = num1 + num2
        print("your result is:",answer)
        print()


    elif operation == "subtract":
        answer = num1 - num2
        print("your result is:",answer)
        print()

    elif operation == "times":
        answer = num1 * num2
        print("your result is:",answer)
        print()


    elif operation == "divide":
        answer = num1 / num2
        print("your result is",answer)
        print()


    else:
        print("dont you know anything in math c'mon")
        print()

    print("thank you for using the program :) ")
