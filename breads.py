t = int(input())

for i in range(t):
    n,m,k = list(map(int,input().split()))
    if(m*k>=n):
        print('Yes')
    else:
        print('No')