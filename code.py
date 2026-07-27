num1 = int(input("enter a number : " ))
task = input("enter your task symble (eg- +,-,*,/) :")
num2 = int(input("enter a number:"))
if task == "+":
    sum = num1 + num2 
    print("here is your sum :" ,sum)
elif task == "-":
    diff = num1 - num2 
    print("here is diffrence :" ,diff)
elif task == "*":
    multi = num1 * num2 
    print("here is product:", multi)
elif task == "/" :
    if num2 == 0 :
        print("bro you can't divide by zero")
    elif type(num1 / num2) == int:
        floor_division = num1 // num2
        print(floor_division)
    else:    
        divide = num1 / num2
        print("here is your divide :" ,divide)
else :
    print ("task is not veild")


