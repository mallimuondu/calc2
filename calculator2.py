import re
# difine my function
def calculator():
     
    operations = input('''
    pleas type in the math oppeeration you will like to complite
    + for additon
    - for subtruction
    * for multiplication
    / for division
    ''')
    
    if not re.match("^[+,-,*,/]*$", operations):
        print("Error! You have put the wrong input")
        calculator()
          
    elif operations == "":
        print("Please select one of the above ")
        calculator()


        #ask user for imput
    number1 = input("enter your first number: ")
    number2 = input("enter your second number: ")
    
    if not re.match("^[0 - 9]*$",number1):
        print("please input a number")
        calculator()
        #Adding operations

        #addition
    if operations == '+':
            print("{} + {} = ".format(number1,number2))
            print(number1 + number2)

        #subtraction
    elif operations == '-':
            print("{} - {} = ".format(number1,number2))
            print(number1 - number2)

        #multiplicaton
    elif operations == '*':
            print("{} * {} = ".format(number1,number2))
            print(number1 * number2)

        #divide
    elif operations == '/':
            print("{} / {} = ".format(number1,number2))
            print(number1 / number2)

    else:
             print("you have not typed a value operator,please run the progrum again")
calculator()        
#define function to ask user if they want to use the calculator again

def again():
    #tacke an input from user
    calc = input('''
    doo you want to claculat again?
    please type y for yes or n no
    ''')
    #acept y in lower case or lower case
    
    if calc.upper()=="Y" :
        calculator()
    elif calc.upper()=="N":
        print("see you later")
    else:
        again()
        
again()