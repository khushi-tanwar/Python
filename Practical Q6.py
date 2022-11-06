'''Consider a tuple t1={1,2,5,7,9,2,4,6,8,10}. Write a program to perform following operations:
a) Print another tuple whose values are even numbers in the given tuple.
b) Concatenate a tuple t2={11,13,15} with t1.
c) Return maximum and minimum value from this tuple.'''

t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)
et= ()
for i in t1:
    if i%2 == 0:
        et+=(i,)
print('Even Tuple:',et)
ct=t1+t2
print('Concatenated Tuple:',ct)
print('Max Value:',max(ct))
print('Min Value:',min(ct))
