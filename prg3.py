'''
    - sum of squares of n odd numbers
'''

n = int(input())
sum = 0

for i in range(1,n+1):
    if(i%2 == 1):
        i = i**2
    sum = sum + i
    print(sum)