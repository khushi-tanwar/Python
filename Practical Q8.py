'''Write a python program to perform the following using list:
a) Check if all elements in list are numbers or not.
b) If it is a numeric list, then count number of odd values in it.
c) If list contains all strings, then display largest string in the list.
d) Display list in reverse form.
e) Find a specified element in list.
f) Remove the specified element from the list.
g) Sort the list in descending order.
h) Accept 2 lists and find the common members in them.'''

def numericlist(l):
    for i in range(0,len(l),1):
        if not l[i].isnumeric():
            return False
    return True

def stringlist(l):
    for i in range(0, len(l),1):
        if not type(l[i]==str):
            return False
    return True

def revDisplay():
    for i in range(0,len(l),1):
        if l[i]==e:
            return True
    return False

def linearSearch(e,l):
    for i in range(0,len(l),1):
        if l[i]==e:
            return True
    return False

def removeElement(e,l):
    if (linearSearch(e,l)):
        l.remove(e)
        return True
    return False

def revSort(l):
    for i in range(0, len(l),1):
        for j in range(i+1, len(l),1):
            if l[i]<l[j]:
                l[i],l[j] = l[j],l[i]
    return l

def displaycommon(l1,l2):
    for i in l1:
        if i in l2:
            print(i, end=' ')
    print()
    
l=[]
l2=[]
r=0
e=0
c=0
r=int(input('Enter range: '))
for i in range(0,r,1):
    e=input('Enter element:')
    l.append(e)
print('List:', end=' ')
print(l)

if (numericlist(l)):
    print('Numeric List')
    for i in l:
        if not int(i)%2 == 0:
            c+=1
    print('No. of odd values in list:',c)
elif (stringlist(l)):
    print('Largest String in list:',max(l))
print('Reversed List:',end=' ')
revDisplay()

e=input('Enter element to search:')
if(linearSearch(e,l)):
    print('Element found in list')
else:
    print('Element not found in list')
    
e= input('Enter Element to remove:')
r= removeElement(e,l)
if(r):
    print('After removed elements:')
else:
    print('Element not found in list')
    
print('Descending Sorted List:',revSort(l))

print('Enter list2:')
r=int(input('Enter a range:'))
for i in range(0,r,1):
    e=input('Enter Element:')
    l2.append(e)
print('Common Elements:',end=' ')
displaycommon(l,l2)

    
