option = input("what are you want? (option - normal calculator , trigonomatric calculator) :")
if option == "normal calculator":
    num1 = int(input("enter your first number :"))
    task = input("enter your task symbol (eg- +,-,*,/,power(**),square root(sqrt)):")
    if task=="sqrt" or task=="square root" or task=="square root(sqrt)":
        square_root=num1**(.5)
        print("square root:",square_root)
        exit()
    else:    
        num2=int(input("enter your second number:"))
    if task=="+":
        total=num1+num2 
        print("total:",total)
    elif task=="-":
        difference=num1-num2 
        print("difference:",difference)
    elif task=="*":
        product=num1*num2 
        print("product:",product)
    elif task=="/":
        if num2==0:
            print("bro you can't divide by zero")
        elif (num1 % num2)!=0 :
            result_type1=input("What kind of answer do you want?(eg. floor division , modulus and division):")
            if result_type1=="floor division":
                floor_division=num1//num2
                print("floor division:",floor_division)
            elif result_type1=="modulus":
                modulus=num1%num2
                print("modulus:",modulus)
            elif result_type1=="division":
                division=num1/num2
                print("division:",division)
        else:    
            quotient=num1/num2
            print("quotient:",quotient)
    elif task=="**" or task=="power" or task=="power(**)":
        power=num1**num2
        print(num1,"to the power of",num2,"is",power)
elif option == "trigonomatric calculator":
    trig_id = str(input("enter your trigonometric identity(eg. sin,cos,ten,cot,sec,cosec):" ))
    angle = str(input("enter angle(eg. 0,30,45,60,90): "))
    if trig_id == "sin" and angle == "0" :
        print("0")
    elif trig_id == "sin" and angle == "30" :
        print("0.5")
    elif trig_id == "sin" and angle == "45" :
        print("0.70710")
    elif trig_id == "sin" and angle == "60" :
        print("0.86602")
    elif trig_id == "sin" and angle == "90" :
        print("1")
    elif trig_id == "cos" and angle == "90" :
        print("0")
    elif trig_id == "cos" and angle == "60" :
        print("0.5")
    elif trig_id == "cos" and angle == "45" :
        print("0.70710")
    elif trig_id == "cos" and angle == "30" :
        print("0.86602")
    elif trig_id == "cos" and angle == "0" :
        print("1")
    elif trig_id == "tan" and angle == "0" :
        print("0")
    elif trig_id == "tan" and angle == "30" :
        print("0.57735")
    elif trig_id == "tan" and angle == "45" :
        print("1")
    elif trig_id == "tan" and angle == "60" :
        print("1.73205")
    elif trig_id == "tan" and angle == "90" :
        print("undefined")
    elif trig_id == "cot" and angle == "90" :
        print("0")
    elif trig_id == "cot" and angle == "60" :
        print("0.57735")
    elif trig_id == "cot" and angle == "45" :
        print("1")
    elif trig_id == "cot" and angle == "30" :
        print("1.73205")
    elif trig_id == "cot" and angle == "0" :
        print("undefined")
    elif trig_id == "sec" and angle == "0" :
        print("1")
    elif trig_id == "sec" and angle == "30" :
        print("1.15470")
    elif trig_id == "sec" and angle == "45" :
        print("1.41421")
    elif trig_id == "sec" and angle == "60" :
        print("2")
    elif trig_id == "sec" and angle == "90" :
        print("undefined")
    elif trig_id == "cosec" and angle == "90" :
     print("1")
    elif trig_id == "cosec" and angle == "60" :
        print("1.15470")
    elif trig_id == "cosec" and angle == "45" :
        print("1.41421")
    elif trig_id == "cosec" and angle == "30" :
        print("2")
    elif trig_id == "cosec" and angle == "0" :
        print("undefined")
    else :
        print("sorry i'm not capable for this calculation.")
