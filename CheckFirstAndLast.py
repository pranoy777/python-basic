list = ['abca','xyzx','aba','122']
count = 0
for x in list:
    if x[0]==x[-1]:
        count+=1
print("total words are:",count)
