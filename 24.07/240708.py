# 가로수
# 문제
# 직선으로 되어있는 도로의 한 편에 가로수가 임의의 간격으로 심어져있다. KOI 시에서는 가로수들이 모두 같은 간격이 되도록 가로수를 추가로 심는 사업을 추진하고 있다. KOI 시에서는 예산문제로 가능한 한 가장 적은 수의 나무를 심고 싶다.

# 편의상 가로수의 위치는 기준점으로 부터 떨어져 있는 거리로 표현되며, 가로수의 위치는 모두 양의 정수이다.

# 예를 들어, 가로수가 (1, 3, 7, 13)의 위치에 있다면 (5, 9, 11)의 위치에 가로수를 더 심으면 모든 가로수들의 간격이 같게 된다. 또한, 가로수가 (2, 6, 12, 18)에 있다면 (4, 8, 10, 14, 16)에 가로수를 더 심어야 한다.

# 심어져 있는 가로수의 위치가 주어질 때, 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 구하는 프로그램을 작성하라. 단, 추가되는 나무는 기존의 나무들 사이에만 심을 수 있다.

# 입력
# 첫째 줄에는 이미 심어져 있는 가로수의 수를 나타내는 하나의 정수 N이 주어진다(3 ≤ N ≤ 100,000). 둘째 줄부터 N개의 줄에는 각 줄마다 심어져 있는 가로수의 위치가 양의 정수로 주어지며, 가로수의 위치를 나타내는 정수는 1,000,000,000 이하이다. 가로수의 위치를 나타내는 정수는 모두 다르고, N개의 가로수는 기준점으로부터 떨어진 거리가 가까운 순서대로 주어진다.

# 출력
# 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 첫 번째 줄에 출력한다.

# 풀이
# 입력
import sys
input = sys.stdin.readline
n = int(input())

# 가로수의 최대간격은 임시 가로수의 최소 간격보다 작거나 같아야한다
# 그러므로 임시가로수의 최소 간격 부터 가로수를 심어본다.
my_list = []
for _ in range(n):
    my_list.append(int(input()))
# 4
# 1
# 3
# 7
# 13
tum = my_list[1] - my_list[0] # = 2
# print(tum)
min_tree = 100000

while tum >= 1:
    dict = {}
    # 딕셔너리 생성
    for i in range(my_list[0],my_list[n-1]):
        if i in my_list:
            dict[i] = 1
        else:
            dict[i] = 0
    # print(f'빈 딕셔너리 생성: {dict}')
    # 임시 가로수 심기
    # for i in my_list:
    #     dict[i] = 1
    # print(f'임시 가로수 심기: {dict}')   
    # 최대 간격부터 간격을 줄여가며 가로수를 배치
    total = 0 # 새로 심은 가로수의 수
    for i in range(my_list[0],my_list[n-1],tum):
        # 가로수가 있으면 다음으로
        if dict[i] == 1:
            continue
        # 없으면 심고 total + 1
        else:
            dict[i] = 1
            total += 1
    print(f'가로수 배치{dict}')
    # 검사
    # 가로수의 간격이 모두 tum과 일치하면서 심어지면 일단 최소 가로수의 개수에 추가된 가로수를 저장
    cnt = 0
    for i in dict:
        # 가로수 없으면 
        if dict[i] == 0:
            cnt += 1
        # 가로수가 심어져 있으면
        elif dict[i] == 1:
            cnt = 0
        if cnt >= tum:
            tum -= 1
            break
    tum -= 1
    min_tree = total
print(min_tree)

# 해당 풀이는 문제를 풀수는 있으나 시간 초과로 실패~

# 더 빠른 풀이를 찾아야한다.
# 모든 간격들의 최대공약수를 찾으면 쉽게 최소 가로수의 개수를 알수있다.
import sys
import math
input = sys.stdin.readline
n = int(input())

tree_positions = [int(input()) for _ in range(n)]

# 각 가로수 사이의 간격을 계산
gaps = []
for i in range(1, n):
    gaps.append(tree_positions[i] - tree_positions[i - 1])

# 모든 간격의 최대공약수를 구함
gcd_gap = gaps[0]
for gap in gaps[1:]:
    gcd_gap = math.gcd(gcd_gap, gap)

# 간격이 gcd_gap이 되도록 가로수를 심기 위해 필요한 추가 가로수의 수를 계산
total_trees_needed = 0
for gap in gaps:
    total_trees_needed += (gap // gcd_gap) - 1

print(total_trees_needed)

