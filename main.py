while True:
    print("Write first number a=")
    a = int(input())

    print("Write second number b=")
    b = int(input())

    print("Choose operation")
    print("1 - to add a+b")
    print("2 - subtract a-b")
    print("3 - multiplication a*b")
    print("4 - division a/b")

    d = int(input())

    if d==1:
        print("Sum a+b=",a+b)
    elif d==2:
        print("Difference a-b=",a-b)
    elif d==3:
        print("Product a*b=",a*b)
    elif d==4:
        if b !=0 and a !=0:
            print("Fraction a/b=",a/b)
        else:
            print("You can't divide by 0")

    s=(input("Do you want to do next operation?(Y/N): "))
    if s=="Y":
        print()

    if s=="N":
        break