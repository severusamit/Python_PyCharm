numbers=[5,2,1,7,4,5,2,9]
#numbers.append(20)
#print(numbers)
#numbers.insert(0,6)
#print(numbers)
uniques=[]
for i in numbers :
    if i not in uniques :
        uniques.append(i)
print(uniques)