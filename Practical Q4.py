def setofDigits(n):
    s=set()
    while n!=0:
        s.add(n%10)
        n//=10
    return s
n=int(input("Enter a number:"))
print('Set of digits:',setofDigits(n))
