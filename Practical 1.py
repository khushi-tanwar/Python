#Write a function that takes the lengths of three sides: side1, side2 and side3 of the triangle as the input from the user using the input function and return
#the area and perimeter of the triangle as a tuple. Also, assert that the sum of the length of any two sides is greater than the third side.


import math
def compute(a,b,c):
    s=(a+b+c)/2.0
    a1=s*(s-a)*(s-b)*(s-c)
    area=math.sqrt(a1)
    perimeter=a+b+c
    a2=(area,perimeter)
    return a2
def main():
    ch="y"
    while (ch=="y"):
        side1=int(input("Enter Side1:"))
        side2=int(input("Enter Side2:"))
        side3=int(input("Enter Side3:"))
        assert side1+side2>side3 and side2+side3>side1 and side1+side3>side2,"Error!!!! Invalid sides"
        print(compute(side1,side2,side3))
        ch=input("Do you want to continue(y/n):")
if __name__=='__main__':
    main()
