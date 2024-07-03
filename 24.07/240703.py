# 듣보잡
# 문제
# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.

# 풀이
# 입력
import sys
input = sys.stdin.readline
# 듣못사 = N , 보못사 = M
N , M = map(int,input().strip().split())

# 듣못사 입력
dict = {}
for _ in range(N):
    dict[input().strip()] = 0

# 보못사 입력
cnt = 0 # 듣보 수
듣보 = [] # 듣보만 모으기 위한 리스트
for _ in range(M):
    bo = input().strip()
    # 만약 보못사가 듣못사 안에 있다면
    if bo in dict: 
        # 듣보 명단에 추가후
        듣보.append(bo) 
        # 듣보 수 +1
        cnt += 1
print(cnt)
sorted_듣보 = sorted(듣보)
for i in sorted_듣보:
    print(i)

# 다른 풀이
# set() 집합을 활용

import sys
input = sys.stdin.readline
# 듣못사 = N , 보못사 = M
N , M = map(int,input().strip().split())

# 듣못사 입력
un_listen = set()
for _ in range(N):
    un_listen.add(input().strip())
# 보못사 입력
un_look = set()
for i in range(M):
    un_look.add(input().strip())

# 두 집합의 합집합 
deotbo = un_listen.intersection(un_look)
# 리스트로 변환 후 정렬
deotbo = sorted(list(deotbo))
# 출력
print(len(deotbo))
for i in deotbo:
    print(i)
# 첫 번째 풀이 보다 속도도 빠르고 코드도 보기 좋은거 같다
