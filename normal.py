class Number :
        def __init__(self, value):
            self.value = value
        def add(self, other):
            return self.value + other.value
        def subtract(self, other):
            return self.value - other.value
        def multiply(self, other):
            return self.value * other.value
        def divide(self, other):
            if other.value == 0:
                return print("Error: Division by zero")
            elif self.value % other.value != 0:
                result_type1 = input("What kind of answer do you want?(eg. floor division , modulus and division):")
                if result_type1 == "floor division":
                    print("Floor Division:", self.value // other.value)
                elif result_type1 == "modulus":
                    print("Modulus:", self.value % other.value)
                elif result_type1 == "division":
                    print("Division:", self.value / other.value)
            else:
                return self.value / other.value
    s1 = Number(int(input("enter a number: ")))
    symbol = input("Enter the operation you want to perform (+, -, *, /,**,sqrt): ")
    if symbol == "sqrt":
        if s1.value < 0:
            print("Square root of negative number is not supported")
        else:
            print("Square root:", s1.value ** 0.5)
        exit()
    s2 = Number(int(input("enter a number: ")))
    if symbol == "+":
        print("Addition:", s1.add(s2))
    elif symbol == "-":
        print("Subtraction:", s1.subtract(s2))
    elif symbol == "*":
        print("Multiplication:", s1.multiply(s2))
    elif symbol == "/":
        result = s1.divide(s2)
        if result is not None:
            print("Division:", result)
    elif symbol == "**":
        print("Exponentiation:", s1.value ** s2.value)
