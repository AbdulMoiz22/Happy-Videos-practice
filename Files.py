Moiz_file= open('Moiz','r')
for m in Moiz_file.readlines():
    print(m)

Moiz_file.close()

#writing to files:
'''Moiz_file= open('Moiz','w')
Moiz_file.write('\nI love me')

Moiz_file.close()'''

Moiz_file = open('index.html','w')
Moiz_file.write('HELLO')
Moiz_file.close()



