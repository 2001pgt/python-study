# 풍선 터뜨리기
# 문제
# 1번부터 N번까지 N개의 풍선이 원형으로 놓여 있고. i번 풍선의 오른쪽에는 i+1번 풍선이 있고, 왼쪽에는 i-1번 풍선이 있다. 단, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다. 각 풍선 안에는 종이가 하나 들어있고, 종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다. 이 풍선들을 다음과 같은 규칙으로 터뜨린다.

# 우선, 제일 처음에는 1번 풍선을 터뜨린다. 다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다. 양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다. 이동할 때에는 이미 터진 풍선은 빼고 이동한다.

# 예를 들어 다섯 개의 풍선 안에 차례로 3, 2, 1, -3, -1이 적혀 있었다고 하자. 이 경우 3이 적혀 있는 1번 풍선, -3이 적혀 있는 4번 풍선, -1이 적혀 있는 5번 풍선, 1이 적혀 있는 3번 풍선, 2가 적혀 있는 2번 풍선의 순서대로 터지게 된다.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000)이 주어진다. 다음 줄에는 차례로 각 풍선 안의 종이에 적혀 있는 수가 주어진다. 종이에 0은 적혀있지 않다.

# 출력
# 첫째 줄에 터진 풍선의 번호를 차례로 나열한다.

# 풀이
import sys
from collections import deque
input = sys.stdin.readline


# 덱 구현
def frontin(deque,x):
    deque.insert(0,x)

def backin(deque,x):
    deque.append(x)

def frontpop(deque):
    if len(deque) == 0:
        print(-1)
    else:
        deque.popleft()

def backpop(deque):
    if len(deque) == 0:
        print(-1)
    else:
        deque.pop()

def get_deque(deque):
    print(len(deque))

def isempty(deque):
    if len(deque) == 0:
        print(1)
    else:
        print(0)

def get_front(deque):
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[0])

def get_back(deque):
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[-1])

# 입력
N = int(input())
# 풍선 순서와 풍선 종이 숫자를 가진 덱을 각각 생성해준다
balloon = deque(map(int,input().rstrip().split()))
array = deque(range(1,N+1))
# 삭제된 풍선의 순서를 담을 리스트
result = []
cnt = 0
# 구현
while(True):
    if len(array) <= 1:
        result.append(array[0])
        print(*result) # []생략하고 출력
        break
    if cnt == 0:
        # 풍선 종이의 숫자 변수에 입력
        num = balloon[0]
        # 풍선 순서 결과 리스트에 추가
        result.append(array[0])
        # 각각의 덱에서 해당 인자들 삭제
        frontpop(balloon)
        frontpop(array)
        # 종이의 숫자 부호 판단 후 부호에 따라 덱 재정비

    # 양수 일때
    if num > 0:
        # 왼쪽으로 숫자를 num-1번 순환
        for _ in range(num-1):
            # 종이 숫자
            backin(balloon,balloon[0])
            frontpop(balloon)
            # print(f'현재 종이 배열 상태{balloon}')
            # 풍선 순서
            backin(array,array[0])
            frontpop(array)
            # print(f'현재 풍선 순서 {array}')

         # 풍선 종이의 숫자 변수에 입력
        num = balloon[0]
        # 풍선 순서 결과 리스트에 추가
        result.append(array[0])
        frontpop(balloon)
        frontpop(array)
    # 음수 일때
    elif num < 0:
        # 오른쪽으로 숫자를 (절대값 num) -1 번 순환
        for _ in range(abs(num)-1):
            # 종이 숫자
            frontin(balloon,balloon[-1])
            backpop(balloon)
            # print(f'현재 종이 배열 상태{balloon}')
            # 풍선 순서
            frontin(array,array[-1])
            backpop(array)
            # print(f'현재 풍선 순서 {array}')   
         # 풍선 종이의 숫자 변수에 입력
        num = balloon[-1]
        # 풍선 순서 결과 리스트에 추가
        result.append(array[-1])
        backpop(balloon)
        backpop(array)
    cnt += 1    