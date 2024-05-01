#별찍기 7 2444
#나의 풀이
N = int(input())

for i in range(N-1,-1,-1):
    print(' '*i,end='')
    for i2 in range(1):
        print('*'*((2*((N-1)-i))+1))

for i in range(1,N):
    print(' '*i,end='')
    for i2 in range(1):
        print('*'*(2*((N-1)-i)+1))
# 다른 풀이
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1))
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))
#==================================================

#펠린드롬인지 확인 10988
n = list(input())
Answer = 1
for i in range(len(n)//2):
    if n[i] !=n[-(i+1)]:
        Answer = 0
        break
print(Answer)

