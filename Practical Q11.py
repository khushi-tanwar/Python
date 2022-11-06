'''Write a menu-driven program to accept a list of students names and perform the following:
a) Search an element using linear search/ binary search.
b) Sort the elements using bubble sort/ Insertion sort sort/ selection sort.'''

def linearSearch(list,e):
    for l in list:
        if e==l:
            return True
    return False

def binarySearch(list,left,right,e):
    if right>=left:
        mid=(left+right)//2
        if list[mid] == e:
            return mid
        elif list[mid]>e:
            return binarySearch(list,left,mid-1,e)
        else:
            return binarySearch(list,mid+1,right,e)
    else:
        return -1

def bubbleSort(list):
    list = list.copy()
    for i in range(len(list)-1):
        for j in range(0,len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

def insertionSort(list):
    list=list.copy()
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    return list

def selectionSort(list):
    list=list.copy()
    for i in range(len(list)):
        min=i
        for j in range(i+1,len(list)):
            if list[min]>list[j]:
                min=j
        list[i],list[min]=list[min],list[i]
    return list

s= []
r = int(input('Enter number of students:'))
for i in range(1,r+1,1):
    n= input('Enter Name:')
    s.append(n)
while True:
    print('''
      MENU
1. Linear Search
2. Binary Search
3. Bubble Sort
4. Insertion Sort
5. Selection Sort
6. Exit
''')
    c= int(input('Enter your choice:'))
    if c==1:
        n=input('Enter name to search:')
        if (linearSearch(s,n)):
            print('Student Found in list')
        else:
            print('Student Not Found')
    elif c==2:
        n=input('Enter name to search:')
        if (binarySearch(bubbleSort(s),0,r-1,n)>=0):
            print('Student Found in list')
        else:
            print('Student Not Found')
    elif c==3:
        print('Original list:',s)
        print('Sorted list:',bubbleSort(s))
    elif c==4:
        print('Original list:',s)
        print('Sorted list:',insertionSort(s))
    elif c==5:
        print('Original list:',s)
        print('Sorted list:',selectionSort(s))
    elif c==6:
        break
    input('Press any key to continue')
    
        
        
                                            
