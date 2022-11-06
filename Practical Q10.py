'''Write a function that takes a sentence as input from the user and calculates the frequency of each letter.
Use a variable of dictionary type to maintain the count.'''

f= dict()
s= input('Enter a sentence:')
for l in s:
    if not l.isalpha():
        continue
    if l not in f:
        f[l]=1
    else:
        f[l]+=1
print('Frequencies:')
for l in f:
    print(f'{l} => {f[l]}')
        
