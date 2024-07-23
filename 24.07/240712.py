# 소수 구하기 1929
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 풀이
# 입력
import sys
input = sys.stdin.readline

M,N = map(int,input().split())

# 어제 사용했던 소수 판별함수를 이용하여 소수를 판별
def Check_sosu(x):
    if x < 2:  # 0과 1은 소수가 아님
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

for i in range(M,N+1):
    # 출력
    if Check_sosu(i) == True: # 소수가 맞으면
        print(i) # 출력
    # 아니면
    else:
        pass # 통과
