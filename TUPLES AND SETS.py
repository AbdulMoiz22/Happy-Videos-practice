#A tuple is a collection which is ordered and unchangeable.Allows duplicate members.

#create tuple by constructor
fruits = tuple(('Apples', 'Orange'))
print(fruits)
#if you want to make a tuple of one value only then also you have tou use ',' otherwise it will treat it as a string only.
#get value
print(fruits[0])
#del tuple
#del fruits
#print(fruits)

#get length
#print(len(fruits))

#A set is a collection which is unordered and unindexed and doesnot support duplicates
fruits_set = {'Apples','Oranges','Mango'}

#Check if in set
#print('Apples' in fruits_set)

fruits_set.add('grapes')
print(fruits_set)

fruits_set.remove('grapes')
print(fruits_set)

fruits_set.clear()

print(fruits_set)




