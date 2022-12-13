salary = int(input())

if(salary>=0 and salary<=150000):
    print('no tax')

if(salary>=150001 and salary<=300000):
    print(0.1 * salary)

if(salary>=300001 and salary<=500000):
    print(0.2 * salary)

if(salary>=500001):
    print(0.3 * salary)