# 도키도키 간식드리미
# 문제
# 인하대학교 학생회에서는 중간, 기말고사 때마다 시험 공부에 지친 학우들을 위해 간식을 나눠주는 간식 드리미 행사를 실시한다. 승환이는 시험 기간이 될 때마다 간식을 받을 생각에 두근두근 설레서 시험 공부에 집중을 못 한다. 이번 중간고사에서도 역시 승환이는 설레는 가슴을 안고 간식을 받기 위해 미리 공지된 장소에 시간 맞춰 도착했다. 그런데 이게 무슨 날벼락인가! 그 곳에는 이미 모든 학생들이 모여있었고, 승환이는 마지막 번호표를 받게 되었다. 설상가상으로 몇몇 양심에 털이 난 학생들이 새치기를 거듭한 끝에 대기열의 순서마저 엉망이 되고 말았다. 간식을 나눠주고 있던 인규는 학우들의 터져 나오는 불만에 번호표 순서로만 간식을 줄 수 있다고 말했다. 

# 그제야 학생들이 순서대로 줄을 서려고 했지만 공간이 너무 협소해서 마음대로 이동할 수 없었다. 다행히도 대기열의 왼쪽에는 1열로 설 수 있는 공간이 존재하여 이 공간을 잘 이용하면 모두가 순서대로 간식을 받을 수 있을지도 모른다. 자칫 간식을 못 받게 될지도 모른다는 위기감을 느낀 승환이는 자신의 컴퓨터 알고리즘적 지식을 활용해 과연 모든 사람들이 순서대로 간식을 받을 수 있는지 확인하는 프로그램을 만들기로 했다. 만약 불가능 하다면 승환이는 이번 중간고사를 망치게 될 것 이고 가능하다면 힘을 얻어 중간고사를 잘 볼 수 있을지도 모른다.

# 사람들은 현재 1열로 줄을 서있고, 맨 앞의 사람만 이동이 가능하다. 인규는 번호표 순서대로만 통과할 수 있는 라인을 만들어 두었다. 이 라인과 대기열의 맨 앞 사람 사이에는 한 사람씩 1열이 들어갈 수 있는 공간이 있다. 현재 대기열의 사람들은 이 공간으로 올 수 있지만 반대는 불가능하다. 승환이를 도와 프로그램을 완성하라.

# 현재 간식 배부 공간을 그림으로 나타내면 다음과 같다.
# 위 예제는 다음 그림과 같이 움직였을 때 모두가 순서대로 간식을 받을 수 있다..



# 입력
# 입력의 첫째 줄에는 현재 승환이의 앞에 서 있는 학생들의 수 N(1 ≤ N ≤ 1,000,자연수)이 주어진다.

# 다음 줄에는 승환이 앞에 서있는 모든 학생들의 번호표(1,2,...,N) 순서가 앞에서부터 뒤 순서로 주어진다.

# 출력
# 승환이가 무사히 간식을 받을 수 있으면 "Nice"(따옴표는 제외)를 출력하고 그렇지 않다면 "Sad"(따옴표는 제외)를 출력한다.

# 풀이 
# 1열 공간을 스택으라고 할 때
# 스택안은 큰수가 더 안쪽에 있어야한다
# 대기열에서 231 같이 대기열 순서가 되면 무조건 불가능

# 가장 작은 수의 앞에 2개이상의 수가 있고 앞의 두 수 중 큰것이 뒤에 있따면 불가능
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
        return 1000000
    else:
        return stack[-1]
# 대기열 숫자
N = int(input().rstrip())

# 대기열 상태
waiting_line = list(map(int,input().rstrip().split()))
print(waiting_line)
 # 가장 작은 수 앞의 모든 수들은 스택에 넣기
    # 여기서 스택에 들어가 있는 숫자들이 크기순으로 되어있지 않다면 sad
    # 크기순으로 들어가 있다면 
    # 가장 작은수를 리스트에서 삭제 
    # 그다음 작은 수는 스택의 맨위의 수와 리스트의 숫자들에서 추출

    # 스택에 있을경우 바로 팝 
    # 리스트에 있을경우 위와 같이 앞에 숫자들을 스택에 넣고 순서 확인
stack = []
cnt = 0
while(True):
    print(f'시작 대기열{waiting_line}')
    print(f'시작 스택{stack}')
    if len(waiting_line) <= 1:
        print("Nice")
        break
    
    # 가장 작은 수 찾기
    min_num = 1001
    for i in range(len(waiting_line)):
        if waiting_line[i] < min_num:
            min_num = waiting_line[i]
            print(f'가장작은수{min_num}')
            min_index = i
            print(f'가장 작은 수의 인덱스{min_index}')
    # 대기열의 가장 작은수와 스택의 맨위의 수 비교 후 더 스택이 더 작으면 스택 한개 팝 후 컨티뉴
    if cnt > 0:
        if min_num > checkstack(stack):
            pop(stack)
            print("================스택이 더 큼으로 삭제후 다시시작 ================== ")
            continue
    # 가장 작은 수 앞의 숫자들 스택에 넣기
    check = False
    for i2 in range(min_index):
        add_stack(stack,waiting_line[i2]) # 스택에 추가
        print(f'현재 스택 {stack}')
    # 스택의 순서를 확인
    for x in range(len(stack)):
        if x > 0:
            if stack[x] > stack[x-1]:
                check = True
                break


    print(check)
    for _ in range(min_index):
        waiting_line.pop(0) # 대기열에서 삭제
        print(f'현재 대기열 {waiting_line}')
    # 스택에 순서대로 들어가지 않으면 종료
    if check == True:
        print("Sad")
        break
    # 스택에 넣은 후 대기열 맨앞 삭제
    waiting_line.pop(0)
    cnt += 1
    print("================루프 완료================== ")

