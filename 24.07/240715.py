# 창문 닫기 13909
# 문제
# 서강대학교 컴퓨터공학과 실습실 R912호에는 현재 N개의 창문이 있고 또 N명의 사람이 있다. 1번째 사람은 1의 배수 번째 창문을 열려 있으면 닫고 닫혀 있으면 연다.  2번째 사람은 2의 배수 번째 창문을 열려 있으면 닫고 닫혀 있으면 연다. 이러한 행동을 N번째 사람까지 진행한 후 열려 있는 창문의 개수를 구하라. 단, 처음에 모든 창문은 닫혀 있다.

# 예를 들어 현재 3개의 창문이 있고 3명의 사람이 있을 때,

# 1번째 사람은 1의 배수인 1,2,3번 창문을 연다. (1, 1, 1)
# 2번째 사람은 2의 배수인 2번 창문을 닫는다. (1, 0, 1)
# 3번째 사람은 3의 배수인 3번 창문을 닫는다. (1, 0, 0)
# 결과적으로 마지막에 열려 있는 창문의 개수는 1개 이다.

# 입력
# 첫 번째 줄에는 창문의 개수와 사람의 수 N(1 ≤ N ≤ 2,100,000,000)이 주어진다.

# 출력
# 마지막에 열려 있는 창문의 개수를 출력한다.

# 풀이

# 입력

import sys
input = sys.stdin.readline

N = int(input())

# 빈 딕셔너리 생성
dict = {}
# 창문 개수 만큼 value가 1인 key값 추가
for i in range(1,N+1):
    dict[i] = 1
# n번째 사람이 n의 배수의 위치한 창문을 열거나 닫는다
# n번째 사람
cnt = 1
num = 2
while cnt <= N:
    for i in range(2,N+1,num):
        if dict[i] == 1:
            dict[i] = 0
        elif dict[i] == 0:
            dict[i] = 1
    num += 1
    print(dict)
    cnt += 1

result = 0
for i in range(1,N+1):
    if dict[i] == 1:
        result += 1
print(result)

# 다른 풀이
# 이 문제는 N 이 21억 개 까지 가능함으로 경우수를 반복해서 답을 찾는 것 보다
# 수학적 규칙을 찾는 것이 올바른 풀이 이다.
import sys
N = int(sys.stdin.readline())
result = 0
x = 1
while x*x <= N:
    x += 1
    result +=1
print(result)

