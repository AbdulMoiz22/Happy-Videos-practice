#LISTS
#by constructor
#numbers = list((1,2,3,4))
#print(numbers)

#getting a value:
'''fruits=['banana','apple','oranges']
fruits[0]='kiwi'
print(fruits)
print(fruits[0])

#get length
print(len(fruits))
#add to list
fruits.append('Mangoes')
print(fruits)
#insert into position
fruits.insert(2,'Strawberries')
print (fruits)




#remove from a position
fruits.pop(2)
print(fruits)

#Reverse list
fruits.reverse()
print(fruits)

#sort
fruits.sort()
print(fruits)'''
number_grid =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
#print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)


