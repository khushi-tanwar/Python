def findLength():
    c=0
    s=input('Enter a String:')
    for i in s:
        c+=1
    print('Length of String:',c)
def maxofString():
    max=''
    s1=input('Enter String 1:')
    s2=input('Enter String 2:')
    s3=input('Enter String 3:')
    if s1>=s2 and s1>=s3:
        max=s1
    elif s2>=s1 and s2>=s3:
        max=s2
    else:
        max=s3
    print("Maximum of three strings:",max)
def replaceVowel():
    s=input('Enter a string:')
    for i in s:
        if i in 'aAeEiIoOuU':
            s=s.replace(i,'#')
    print('Modified String:',s)
def numberofWords():
    s=input('Enter a String:')
    c=0
    for i in s:
        if i==' ':
            c+=1
    print('Number of Words:',c+1)
def palindrome():
    f=True
    s=input('Enter a String:')
    for i in range(0, len(s)//2,1):
        if s[i] != s[len(s)-i-1]:
            f=False
            print('Not Palindrome')
            break
    if f==True:
        print('Palindrome')
s=''
s1=''
s2=''
s3=''
flag=0
while True:
    print('''
         MENU
1. Find length of String
2. Return Maximum of 3 Strings
3. Replace all vowels with #
4. Find number of words in the string
5. Check whether the string is palindrome or not
6. Exit
   ''')
    c = int(input('Enter your choice:'))
    if c==1:
        findLength()
    elif c==2:
        maxofString()
    elif c==3:
        replaceVowel()
    elif c==4:
        numberofWords()
    elif c==5:
        palindrome()
    elif c==6:
        break
    input('Press any key to continue')
                
