# a function is a block of code which runs only when it is called.
#create function
def sayHello(name):
    print(f'Hello {name}')
sayHello ('Moiz')

#return values
def getSum(num1,num2):
    total = num1 + num2
    return total


#A lambda function can take any number of arguements,but can hae only one expression.

getsum= lambda num1,num2 : num1 + num2

print(getsum(1,3))