running = True
while running:
    print("1 = add")
    print("2 = sub")
    print("3 = mul")
    print("4 = div")
    print("5 = exit")
    cmd = int(input("Enter no.: "))
    if cmd == 1:
        print("Add")
        first = int(input("Enter 1st no.: "))
        second = int(input("Enter 2nd no.: "))
        result = first + second
        print first ,'+' ,second ,'=' ,result
    elif cmd == 2:
        print("Sub")
        first = int(input("Enter 1st no.: "))
        second = int(input("Enter 2nd no.: "))
        result = first - second
        print first ,'-' ,second , '=' ,result
    elif cmd == 3:
        print("Mul")
        first = int(input("Enter 1st no.: "))
        second = int(input("Enter 2nd no.: "))
        result = first * second
        print first ,'*' ,second , '=' ,result
    elif cmd == 4:
        print("Div")
        first = int(input("Enter 1st no.: "))
        second = int(input("Enter 2nd no.: "))
        result = first / second
        print first ,'/' ,second , '=' ,result
    elif cmd == 5:
        print("Quit!")
        running = False
    
