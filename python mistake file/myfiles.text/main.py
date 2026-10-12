
#reading file

f= open('myfile.text' , 'r')
text=f.read()
print(text)
f.close()

#writing file

f=open('myfile.text','w')
f.write('hello , world')
f.close()



with open('myfile.text','a') as f:
    f.write("hey i am inside with")
























