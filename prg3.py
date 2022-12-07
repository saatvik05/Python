'''
    - sum of squares of n odd numbers
'''

n = int(input())
sum = 0

for i in range(1,100,2):
    if(i%2 == 1):
        temp = i**2
        sum = sum + temp
        print(sum)
        

    '''
        1. i=0, sum = 0
        2. i=1, temp = 1, sum = 1
        3. 
    '''