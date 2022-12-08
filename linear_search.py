a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 101, 102, 103, 104, 105]

n = int(input())

present = False 

for i in range(0,len(a)):
    if(n==a[i]):
        print(i)
        present = True
if(present==False):
   print('nil')