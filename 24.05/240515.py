#진법변환2 11005

# 문제
# 10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.

# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 10진법 수 N을 B진법으로 출력한다.

#나의 풀이
# 10진수를 변환하고자 하는 진법으로 나눕니다.
# 나머지를 기록합니다.
# 몫을 새로운 10진수로 취급하고 나머지로 나눕니다.
# 위 과정을 나머지가 0이 될 때까지 반복합니다.
# 기록한 나머지를 역순으로 나열하여 최종 결과를 얻습니다.
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N,b =map(int,input().split())

remainder = []
while True:
    remainder.append(N % b)
    if N // b < 1:
        break
    N = N // b
    
remainder = reversed(remainder)
for i in remainder:
    print(ary[i],end='')