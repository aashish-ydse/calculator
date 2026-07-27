num1 = int(input("enter a number : " ))
task = input("enter your task symble (eg- +,-,*,/) :")
num2 = int(input("enter a number:"))
if task == "+":
    sum = num1 + num2 
    print("here is your sum :" ,sum)
elif task == "-":
    diff = num1 - num2 
    print("here is your diffrence :" ,diff)
elif task == "*":
    multi = num1 * num2 
    print("here is your product:", multi)
elif task == "/" :
    if num2 == 0 :
        print("bro you can't divide by zero")
    elif (num1 % num2) != 0 :
        result_type1 = input("What kind of answer do you want?(eg. floor division , modulus):")
        if result_type1 == "floor division":
            floor_division = num1 // num2
            print("here is your floor division : ", floor_division)
        elif result_type1 == "modulus":
            modulus = num1 % num2
            print("here is your modulus :" , modulus)
    else:    
        divide = num1 / num2
        print("here is your divide :" ,divide)
else :
    print ("task is not veild")


