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
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num = int(input())
    # num보다 크거나 같은 소수 중 가장 작은 소수
    # 소수를 판단하는 방법
    # 2부터  루트 N 까지의 모든 홀수로 나눠서 나누어 지지 않으면 소수
    for i in range(num,4000000000):
        if i < 3:
            continue
        elif i % 2 == 0:
            continue

        for x in range()