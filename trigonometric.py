import math 
def run():
    trig_id=str(input("enter your trigonometric identity(eg. sin,cos,tan,cot,sec,cosec):" ))
    angle=float(input("enter angle:"))
    rad = math.radians(float(angle))
    if trig_id=="sin":
        print("sin(",angle,")=",math.sin(rad))
    elif trig_id=="cos":
        print("cos(",angle,")=",math.cos(rad))
    elif trig_id=="tan":
        print("tan(",angle,")=",math.tan(rad))
    elif trig_id=="cot":
        print("cot(",angle,")=",1/math.tan(rad))
    elif trig_id=="sec":
        print("sec(",angle,")=",1/math.cos(rad))
    elif trig_id=="cosec":
        print("cosec(",angle,")=",1/math.sin(rad))
    else:
        print("invalid input")
