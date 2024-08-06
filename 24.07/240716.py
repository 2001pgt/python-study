# 스택 2 28278
# 문제
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
# 입력
# 첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

# 둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.

# 출력을 요구하는 명령은 하나 이상 주어진다.

# 출력
# 출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.

# 풀이
# 자료구조 중 스택을 구현하는 문제이다.

# 입력
import sys
input = sys.stdin.readline
stack = []
N = int(input().strip())

def add_stack(stack,x):
    stack.append(x)
    
def pop(stack):
    if len(stack) == 0:
        return print(-1)
    else:
        print(stack[-1])
        stack.pop()

def getStack(stack):
    return len(stack)

def clean_check_stack(stack):
    if len(stack) == 0:
        return 1
    else:
        return 0
def checkstack(stack):
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]

for _ in range(N):
    # 숫자 입력
    c = input().strip()
    if len(c) == 1:
        a = int(c)
        b = None
    else:
        a = int(c[0])
        b = int("".join(c[-(len(c)-1):]))
    
    # 1 : 정수 X를 스택에 넣는다.
    if a == 1:
        add_stack(stack,b)
    # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    elif a == 2:
        pop(stack)
    # 3: 스택에 들어있는 정수의 개수를 출력한다.
    elif a == 3:
        print(getStack(stack))
    # 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif a == 4:
        print(clean_check_stack(stack))
    # 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    elif a == 5:
        print(checkstack(stack))
# 스택 정복 