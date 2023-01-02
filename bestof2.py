t=int(input())

for i in range(t):
    x,y = list(map(int,input().split()))
    #print(max(x,y))
    
    if(x>y):
        print(x)
    if(x==y or y==x):
        print(x)
    else:
        if(y>x):
            print(y)