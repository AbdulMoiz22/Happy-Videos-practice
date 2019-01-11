#to prevent Value error from breaking your entire program:
try:

    number = int(input('Enter: '))
    print(number)
except ValueError:
    print('error')
