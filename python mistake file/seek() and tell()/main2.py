

with open('samlpe.txt','w') as f:
    f.write('hello world')
    f.truncate(5)


with open('sample.txt','r') as f:
    print(f.read())
























