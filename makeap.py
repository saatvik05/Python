t = int(input())

for i in range(t):
    a,c = list(map(int,input().split()))
    if(a>c):
        print('Enter a less than c')
        break
    else:
        if((a+c)%2==0):
            b=(a+c)//2
        if((b-a)==(c-b)):
            print(b)
        else:
            print(-1)
