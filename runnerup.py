n = int(input())

scores = list(map(int,input().split()))

curr_max = scores[0]

for i in scores:
    if(i>curr_max):
        curr_max = i
    
runnerup_score = -1

for i in scores:
    # if(runnerup_score==curr_max):
    #     continue
    if(i==curr_max):
        continue
    else:
        if(i>runnerup_score):
            runnerup_score = i

print(runnerup_score)
        

 