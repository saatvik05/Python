age = (input())

if type(age) != int:
    print('Enter valid age')
else:   
    if(age < 18):
        print('You\'re still a child')
    else:
        print('Fianlly you\'re above 18')