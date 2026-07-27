num1 = int(input("enter your first number : " ))
task = input("enter your task symbol (eg- +,-,*,/) :")
num2 = int(input("enter your second number:"))
if task == "+":
    total = num1 + num2 
    print("total :" ,total)
elif task == "-":
    difference = num1 - num2 
    print("difference :" ,difference)
elif task == "*":
    product = num1 * num2 
    print("product:", product)
elif task == "/" :
    if num2 == 0 :
        print("bro you can't divide by zero")
    elif (num1 % num2) != 0 :
        result_type1 = input("What kind of answer do you want?(eg. floor division , modulus):")
        if result_type1 == "floor division":
            floor_division = num1 // num2
            print("floor division : ", floor_division)
        elif result_type1 == "modulus":
            modulus = num1 % num2
            print("modulus :" , modulus)
    else:    
        quotient = num1 / num2
        print("quotient :" ,quotient)
else :
    print ("task is not valid")


