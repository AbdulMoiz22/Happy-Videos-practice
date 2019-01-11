 #for loop

people= ['john','paul','sara','susan']

#for person in people:
 #   if person== 'sara':
  #      break
   # print(f'current : {person}')
#if you only want to skip sara
for  person in people:
    if person=='sara':
        continue
    print(f'current : {person}')
#range
#for i in range(len(people)):
#    print(people[i])

#WHILE LOOPS:
count= 0
while count <10:
    print(f'Count = {count}')
    count+=1



