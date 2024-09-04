# 요세푸스 문제 0
# 문제
# 요세푸스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

# 출력
# 예제와 같이 요세푸스 순열을 출력한다.

# 풀이
import sys
from collections import deque
input = sys.stdin.readline

# 큐 구현
def push(queue,num):
    queue.append(num)

def pop(queue):
    queue.popleft()

def size(queue):
    print(len(queue))

def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
def back(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])
# 입력
N, K = map(int,input().rstrip().split())

# 요세푸스 순열 구현
# K 번째 자리 숫자를 제거하기 위해 
# 맨 앞 인자를 뒤로 k-1번 옮긴다.
# 그리고 맨앞의 숫자를 pop한 후 결과 리스트에 옮긴다 
# 또 같은 방법을 반복한다.

# 1~N까지 원형 테이블생성
table = deque(range(1,N+1))
result = []
cnt = 0
while(True):
    if len(table) <= 0:
        print("<",end="")
        for i in range(len(result)):
            print(result[i],end="")
            if i == len(result)-1:
                print(">")
            else:
                print(",",end=" ")
        break
    # 맨앞의 원소를 k-1번 맨 뒤로 이동
    for _ in range(K-1):
        # 맨앞의 원소를 맨 뒤로 이동
        push(table,table[0])
        # 원래 자리의 원소 삭제
        pop(table)
    # 맨 앞 원소를 리스트로 옮긴뒤 pop
    result.append(table[0])
    pop(table)
    

    
