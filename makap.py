t = int(input())

for i in range(t):
    a,c = list(map(int,input().split()))
    b=(a+c)%2
    
    if(b==0):
        print((a+c)//2)
    else:
        print(-1)