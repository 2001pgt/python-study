#다이아몬드 별찍기 2444
#나의 풀이
N = int(input())

#다이아 몬드 위쪽부분
for i in range(N-1,-1,-1):
    print(' '*i,end='')
    for i2 in range(1):
        print('*'*((2*((N-1)-i))+1))

#다이아몬드 아래부분
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
#기본값 설정
Answer = 1

#문자열의 인덱스를 양끝에서 중앙으로 이동하며 해당 인덱스의 값을 비교
for i in range(len(n)//2):
    if n[i] !=n[-(i+1)]:
        Answer = 0
        break
print(Answer)

#다른 풀이
#reversed 함수 사용
n = list(input())
Answer = 1
reversed_n = list(reversed(n)) # 반전된 문자열을 리스트로 변환
if reversed_n != n:
    Answer = 0
print(Answer)

