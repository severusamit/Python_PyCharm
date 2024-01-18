names = ['John','Bob', 'Amit','Sarah','Mosh']
names[0] ="jon"
print(names[2:])
print(names)

print("Find Largest number in a list")

n =int(input("Enter elements of list ?"))
list1 =[]

for i in range(0,n):
    ele =int(input())
    list1.append(ele)
print(list1)
max =list1[0]
for y in list1:
    if y >max:
        max=y

print(max)

