# queuestack
# 문제
# 한가롭게 방학에 놀고 있던 도현이는 갑자기 재밌는 자료구조를 생각해냈다. 그 자료구조의 이름은 queuestack이다.

# queuestack의 구조는 다음과 같다. 
# $1$번, 
# $2$번, ... , 
# $N$번의 자료구조(queue 혹은 stack)가 나열되어있으며, 각각의 자료구조에는 한 개의 원소가 들어있다.

# queuestack의 작동은 다음과 같다.

#  
# $x_0$을 입력받는다.
#  
# $x_0$을 
# $1$번 자료구조에 삽입한 뒤 
# $1$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 
# $x_1$이라 한다.
#  
# $x_1$을 
# $2$번 자료구조에 삽입한 뒤 
# $2$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 
# $x_2$이라 한다.
# ...
#  
# $x_{N-1}$을 
# $N$번 자료구조에 삽입한 뒤 
# $N$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 
# $x_N$이라 한다.
#  
# $x_N$을 리턴한다.
# 도현이는 길이 
# $M$의 수열 
# $C$를 가져와서 수열의 원소를 앞에서부터 차례대로 queuestack에 삽입할 것이다. 이전에 삽입한 결과는 남아 있다. (예제 
# $1$ 참고)

# queuestack에 넣을 원소들이 주어졌을 때, 해당 원소를 넣은 리턴값을 출력하는 프로그램을 작성해보자.

# 입력
# 첫째 줄에 queuestack을 구성하는 자료구조의 개수 
# $N$이 주어진다. (
# $1 \leq N \leq 100\,000$)

# 둘째 줄에 길이 
# $N$의 수열 
# $A$가 주어진다. 
# $i$번 자료구조가 큐라면 
# $A_i = 0$, 스택이라면 
# $A_i = 1$이다.

# 셋째 줄에 길이 
# $N$의 수열 
# $B$가 주어진다. 
# $B_i$는 
# $i$번 자료구조에 들어 있는 원소이다. (
# $1 \leq B_i \leq 1\,000\,000\,000$)

# 넷째 줄에 삽입할 수열의 길이 
# $M$이 주어진다. (
# $1 \leq M \leq 100\,000$)

# 다섯째 줄에 queuestack에 삽입할 원소를 담고 있는 길이 
# $M$의 수열 
# $C$가 주어진다. (
# $1 \leq C_i \leq 1\,000\,000\,000$)

# 입력으로 주어지는 모든 수는 정수이다.

# 출력
# 수열 
# $C$의 원소를 차례대로 queuestack에 삽입했을 때의 리턴값을 공백으로 구분하여 출력한다.

# 풀이
import sys
from collections import deque
input = sys.stdin.readline

# 입력
N = int(input().rstrip())
queuestack = list(map(int,input().rstrip().split()))
array = list(map(int,input().rstrip().split()))
M = int(input().rstrip())
x = list(map(int,input().rstrip().split()))
# 문제를 잘 뜯어보면
# 스택은 원소의 변화가 일어나지 않지만 큐는 일어난다
# 그래서 큐인 원소만 모아서 x값을 넣어보니 이 자체로 큐의 역할을 하게 된다
# 제대로 보면 리스트를 반대로 뒤집은 큐이다
# 예제를 예로 들면 큐는 1,4 이다 그리고 x=2를 넣으면 맨 뒤에 4가 나온다.
# 이제 이 형태를 구현해보도록하자

# 구현

# 우선 큐를 전부 추출
queue = deque()
for i in range(N):
    if queuestack[i] == 0:
        queue.append(array[i])
# 추출한 큐에 인자를 집어넣어 결과를 result에 넣는다
result = []
for i2 in range(M):
    queue.appendleft(x[i2])
    result.append(queue[-1])
    queue.pop()
print(*result)
        
