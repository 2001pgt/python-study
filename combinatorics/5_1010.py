from math import factorial
T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    result = factorial(m)//(factorial(n)*factorial(m-n)) 
    print(result)