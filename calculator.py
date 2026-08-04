#calculator without any errors
def add(*args):
    return sum(args)

def sub(first_num,*args):
    total=first_num
    for num in args:
        total=total-num
    return total

def multiplication(*args):
    total=1.0
    for num in args:
        total=total*num
    return total

def division(first_num,*args):
    total=first_num
    for num in args:
        total=total/num
    return total

def factorial(n):
    total=1
    for i in range(1,n+1):
        total*=i
    return total

print('                                                              ----------CALCULATOR----------')


print("options \n1-addtion \n2-subtraction \n3-multiplication \n4-division \n5-factorial ")
while True:
    user_option=input('choose the options from above = ')
    if user_option not in ["1","2","3","4","5","6"]:
        print('invalid option selected! select valid option')
        continue
    user_option==int(user_option)
    break
if user_option == "1":

    plus=[]
    while True:
        num=input('Enter number for the addtion = ')
        if num == "":
            break
        try:
            plus.append(float(num))
        except ValueError:
            print('invalid input! enter valid number....')
    print("The result for your choosen option(addtion) = ",add(*plus))

elif user_option=="2":
    
    start=input('Enter initial number for the subtraction = ')
    
    try:
        initial=float(start) if start!= "" else 0.0
    
    except ValueError:
        print('invalid input so programm takes 0.0 as input....')
        initial=0.0
    
    minus=[]
    while True:
        num=input('Enter number for the subtraction = ')
        if num =="":
            break
        try:
            minus.append(float(num))
        except ValueError:
            print('invalid input! enter valid number....')
    print("The result for your choosen option(subtraction) = ",sub(initial,*minus))

elif user_option=="3":
    
    cross=[]
    while True:
        num=input('Enter number for the multiplilcation = ')
        if num == "":
            break
        try:
            cross.append(float(num))
        except ValueError:
            print('invalid input! Enter valid numbers....')

    if not cross:
        print('operation cancelled because no inputs were given')
    else:
        print("The result for your choosen option(multiplication) = ",multiplication(*cross))

elif user_option=="4":
    
    first_num=input('Enter number for the division(numerator) = ')
    
    try:
        initial=float(first_num) if first_num!="" else 1.0
    except ValueError:
        print('invalid input so operation takes 1.0 as input....')
        initial=1.0
    
    div=[]
    while True:
        num=input('Enter number for the division(denominator) = ')
        if num == "":
            break
        try:
            val=float(num)

            if val == 0:
                print('cannot divisible by zero....')
                continue
            div.append(val)
        except ValueError:
            print('invalid input! enter valid number....')
    print("The result for your choosen option(division) = ",division(initial,*div))

elif user_option=="5":
    
    while True:
        num_val = input('Enter number for the factorial = ')
        try:
            num=float(num_val)
            if not num.is_integer() or num<0 :
                print('factorial cannot be integes and negatives....')
                continue

            val=int(num)
            break

        except ValueError:
            print('Invalid input enter numeric digits only!')

    print("The result for your choosen option(factorial) = ",factorial(val))

elif user_option=="6":
    print('Exit...bye')
