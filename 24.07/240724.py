# 덱 2
# 문제
# 정수를 저장하는 덱을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여덟 가지이다.

# 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
# 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
# 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 5: 덱에 들어있는 정수의 개수를 출력한다.
# 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
# 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
# 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
# 입력
# 첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

# 둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.

# 출력을 요구하는 명령은 하나 이상 주어진다.

# 출력
# 출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.

import sys
from collections import deque
input = sys.stdin.readline

# 풀이 

# 덱 구현
def frontin(deque,x):
    deque.insert(0,x)

def backin(deque,x):
    deque.append(x)

def frontpop(deque):
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[0])
        deque.popleft()

def backpop(deque):
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[-1])
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

T = int(input().rstrip())
array = deque()
for _ in range(T):
    command = list(input().rstrip().split())
    if command[0] == "1":
        frontin(array,int(command[-1]))
    elif command[0] == "2":
        backin(array,int(command[-1]))         
    elif command[0] == "3":
        frontpop(array)
    elif command[0] == "4":
        backpop(array)
    elif command[0] == "5":
        get_deque(array)
    elif command[0] == "6":
        isempty(array)
    elif command[0] == "7":
        get_front(array)
    elif command[0] == "8":
        get_back(array)









