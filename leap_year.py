'''
     Leap Year - Functions
     -Hacker Rank
     -https://www.hackerrank.com/challenges/write-a-function
'''

n = int(input())

def leapyear(n):
    if(n%4==0 and n%100 !=0 ):
        return True
    elif(n%4==0 and n%100 == 0 and n%400 == 0):
        return True
    else:
        return False
print(leapyear(n))


   