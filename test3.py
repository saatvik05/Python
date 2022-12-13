n = int(input()) #3

c = list(map(int,input().split())) #[2,5,4]
       #2 
cube_list = []

for i in c:   #2  
    if(i%2==0):   
        cube = i*i*i 
        cube_list.append(cube)
        
print(cube_list)