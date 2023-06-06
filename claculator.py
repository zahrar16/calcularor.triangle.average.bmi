from unittest import result

import math

print ("welcom to my calculator")
for i in range(1000):

    print ("summ")
    print ("sub")
    print ("mul")
    print ("div")
    print ("square")
    print ("sin")
    print ("cos")
    print ("tan")
    print ("cotan")
    print ("factorial")
    print ("exit")
    print("please enter your choice")

    operator = input("pls choise your operator :")

    if operator == "exit" or operator == "خروج":
        print("tnks for using my calculator")
        break

    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
        a = float (input("enter first number :"))
        b = float (input("enter second number :"))
    else:
        a = float(input("enter your number : "))


    if operator == "+" or operator == "caret" or operator =="جمع":
        print(a+b)

    elif operator == "-" or operator == "sub" or operator =="تفریق":
        print(a-b)

    elif operator == "*" or operator == "mul" or operator =="ضرب":
        print(a*b)

    elif operator == "/" or operator == "taghsim" or operator =="تقسیم":
        print(a/b)

    elif operator == "**" or operator == "tavan" or operator =="توان":
        print(a**b)

    elif operator == "tanjant" or operator == "tan" or operator =="نانژانت":
        a * 0.0174532925
        print(math.tan(a))

    elif operator == "cotanjant" or operator == "contan" or operator =="کتانژانت":
        a * 0.0174532925
        print(1 / math.tan(a))
        
    elif operator == "sinos" or operator == "sin" or operator =="سینوس":
        a * 0.0174532925
        print(math.sin(a))

    elif operator == "cosinos" or operator == "cos" or operator =="کسینوس":
        a * 0.0174532925
        print(math.cos(a))  

    elif operator == "sqrt" or operator == "sqr" or operator =="جذر":
        print(math.sqrt(a))


    elif operator == "factorial" or operator == "fac" or operator == "فاکتوریل":
        a = int(a)
        factorial = 1
        for i in range (1, a+1):
            factorial = factorial * i
        print ("factoril",a,"barabar ast ba",factorial)     





