# 균형잡힌 세상 4949
# 문제
# 세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.

# 정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

# 문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
# 정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

# 입력
# 각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 이루어져 있으며, 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.

# 입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.
# 출력
# 각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.

import sys
input = sys.stdin.readline

# 스택 구현
def add_stack(stack,x):
    stack.append(x)
def pop(stack):
    if len(stack) == 0:
        return print(-1)
    else:
        stack.pop()
def checkstack(stack):
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]

# 스택을 활용하여 괄호가 완성되면 팝한다
# 구현
# 입력 받은 괄호를 스택형태로 저장한다
# 만약 () 형태가 완성되면 2개를 팝한다
# 그리고 최종적으로 스택에 남은 괄호가 있다면 vps가 아니다
# 스택에 남은 괄호가 없다면 vps이다
# ++++++++++++++++++++++++++++++++++++++++++
# 문자열을 받으면 해당 문자열에서 괄호만 추출해야한다

# 괄호를 추출하는 함수
def choice(str):
    ghalho = []
    for i in range(len(str)):
        if str[i] == "(" or str[i] == ")" or str[i] == "[" or str[i] == "]": 
            ghalho.append(str[i])
    return ghalho

# 구현부
while(True):
    stack = []
    # 입력
    str = input().rstrip()
    # 종료 조건
    if str == ".":
        break
    # 괄호 추출
    check_vps = choice(str)
    # print(check_vps)
    # print(check_vps[0])
    for i in range(len(check_vps)):
        add_stack(stack,check_vps[i])
        # 스택에서 ) 가 들어왔을때 이전에 ( 이 있다면 2개 다 pop 한다.
        if checkstack(stack) == ")"  and len(stack) > 1 and stack[-2] == "(": 
            pop(stack)
            pop(stack)
        elif checkstack(stack) == "]" and len(stack) > 1 and stack[-2] == "[":
            pop(stack)
            pop(stack)
        # print(f'현재 스택{stack}')  
    # print(f'결과 스택{stack}')    
    if len(stack) > 0:
        print("no")
    else:
        print("yes")