# 다음 소수 4134
# 문제
# 정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

# 출력
# 각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.

# 풀이
# 입력
import sys 
import math
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    num = int(input().strip())
    # num보다 크거나 같은 소수 중 가장 작은 소수
    # 소수를 판단하는 방법
    # 2부터  루트 N 까지의 모든 홀수로 나눠서 나누어 지지 않으면 소수
    if num <=2:
            print(2)
            continue
    # 짝수면
    if num % 2 == 0:
         num += 1

    for i in range(num,4000000000,2):
        sosu = True
        # 소수 판별
        for x in range(2,int(i ** 0.5)+1): 
            # 나누어 떨어지지 않으면 통과

            # 나누어 떨어지면 소수 X
            if i % x == 0:
                sosu = False
                # 소수가 아니므로 다음 숫자로 넘어가기
                break
        # 결과가 소수면 추력
        if sosu == True:
            print(i)
            break
# 예시 결과랑 추가로 해본 예시들도 전부 잘되는데 왜 틀렸는지 모르겠다.
# 핵심 부분은 같은거 같은데 어디가 문젠건지...
# 정답
import sys
input=sys.stdin.readline
N=int(input())

def check(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

for i in range(N):
    n=int(input())
    while True:
        if n==0 or n==1:
            print(2)
            break
        if check(n):
            print(n)
            break
        else:
            n+=1