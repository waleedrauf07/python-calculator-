def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

def opt():
    print("********** Select Operation **********")
    print('''
    1. add
    2. subtract
    3. multiply
    4. divide'''
    )
    
while True:
    print()
    opt()
    print()
    choice = input("Enter Choice: (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print()
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multi(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))
        print()
        y_n = input("Do you want to do again or not (Yes/No): ")
        if y_n in ('yes', 'y'):
            
            continue
        else:
            print()
            print("Thanks for using calculator")
            break
    else:
        print('Invalid Input')
