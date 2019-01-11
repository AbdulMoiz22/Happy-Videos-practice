#IF/ELSE

x= 10
y= 8

#if x>y:
 #   print(f'{x} is greater than {y}')
#else:
 #   print('bye')

 #ELIF
if x>y:
    print(f'{x} is greater than {y}')
elif x==y:
    print('EQUAL')
else:
    print('bye')
#Nested if
if x>2:
    if x<=10:
        print(f'{x} is greater than 2 and less than or equal to 10')

#Memership operators

numbers = [1,2,3,4,5,6]

#if x in numbers:
   # print(x in numbers)
if x not in numbers:
    print(x not in numbers)
#identity operators
if x is y:
    print(x is y)
if x is not y:
    print(x is not y)
