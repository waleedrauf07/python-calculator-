while True:
    print()
    print("********** Select Operation **********")
    print('''
    1. add
    2. subtract
    3. multiply
    4. divide'''
    )
    print()
    choice = input("Enter Choice (1/2/3/4): ")
    print()
    if choice in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print()
        if choice == '1':
            print(num1, '+', num2, '=', num1+num2)

        elif choice == '2':
            print(num1, '-', num2, '=', num1-num2)

        elif choice == '3':
            print(num1, '*', num2, '=', num1*num2)

        elif choice == '4':
            print(num1, '/', num2, '=', num1/num2)
        
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
