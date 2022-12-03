"""
   Python If-Else
   -Hacker-rank
   -https://www.hackerrank.com/challenges/py-if-else/problem
"""
n = int(input())

if type(n) != int:
    print('Enter a number')

else:
    if(n%2 == 1):
        print('Weird')
    elif(n>=2 and n<=5):
         print('Not Weird')
    elif(n>=6 and n<=20):
        print('Weird')
    else:
        print('Not Weird')




