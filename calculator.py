"""
Calculator library containing basic math operations
"""

class Calculator:
    def add(self,a,b):
        return a+b 
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
        
calc = Calculator()

#while loop 
while True:
    
    #print statements
    print('1 add')
    print('2 subtract')
    print('3 multiply')
    print('4 divide')
    print('5 exit')

    #input for function
    #choice variable 1-5 exit
    choice = float(input('Choose a function: '))
    #check if choice is valid
    if choice in range(0,6):
        #if choice == 5 break
        if choice == 5:
            break
        a = float(input('First number: '))
        b = float(input('Second number: '))
        if choice == 1:
            print(a, "+", b, "=", calc.add(a,b))
        elif choice == 2:
            print(a, "-", b, "=", calc.subtract(a,b))
        elif choice == 3:
            print(a, "*", b, "=", calc.multiply(a,b))
        elif choice == 4:
            print(a, "/", b, "=", calc.divide(a,b))
    else:
        print('error')
