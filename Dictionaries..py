#A dictionary is a collection which is unordered,changeable and indexed. No duplicate members.

#create dict
person = {
    'first_name': 'Abdul',
    'last_name': 'Moiz',
    'age':30
}
print(person,type(person))

#use constructor
#person2 = dict(first_name='moiz')
#print(person2)

#get value
print(person['first_name'])
print(person.get('first_name'))


#Add key/value
person['phone']= '03212060704'


print(person)

#get keys
print(person.keys())

#get items

print(person.items())

#copy

person2= person.copy()
person2['city']='karachi'
print(person2)
#remove item
del(person['age'])
person.pop('phone')
print(person)

#Clear
person.clear()
print (person)

#get length
print(len(person2))

#List of dict
people = [
    {'name': 'Abdul Moiz','age':30},
    {'name': 'Rushan','age':'70'}
]
print(people[0])
print(people[0]['age'])

