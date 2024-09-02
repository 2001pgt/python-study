# 괄호 9012   
# 문제
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

# 입력
# 입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

# 출력
# 출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 

# 풀이
# 입력
import sys
input = sys.stdin.readline

T = int(input()) # 테스트 횟수

# 스택
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
for _ in range(T):
    stack = []
    check_vps = input().strip()
    # print(check_vps)
    # print(check_vps[0])
    for i in range(len(check_vps)):
        add_stack(stack,check_vps[i])
        if checkstack(stack) == ")"  and len(stack) > 1 and stack[-2] == "(":
            pop(stack)
            pop(stack)
        # print(f'현재 스택{stack}')  
    # print(f'결과 스택{stack}')    
    if len(stack) > 0:
        print("NO")
    else:
        print("YES")

    
        