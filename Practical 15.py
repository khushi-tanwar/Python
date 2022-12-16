#Define a class Student to store his/her name and marks in three subjects.Use a variable to store the maximum average marks of the class. Use constructor and 
#destructor to initialize and destroy the objects.


class Student(object):
    def __init__(self):
        self.name=input("Enter the name of student:")
        self.sub1=int(input("Marks in 1st Subject:"))
        self.sub2=int(input("Marks in 2nd Subject:"))
        self.sub3=int(input("Marks in 3rd Subject:"))
        self.avg=(self.sub1+self.sub2+self.sub3)/3
    def __del__(self):
        print("Student with name",self.name,"is deleted")
print("Enter the number of students in class:")
n=int(input())
max=0
i=0
s=[1]*n
for i in range(0,n):
    s[i]=Student()
for i in range(0,n):
    print(s[i].name," ",s[i].avg)
for i in range(0,n):
    if(s[i].avg>max):
        max=s[i].avg
print("Highest average marks in class is",max)
for i in range(0,n):
    s[i].__del__()
