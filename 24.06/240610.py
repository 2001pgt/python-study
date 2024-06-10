# 좌표 정렬하기 11650
# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

# 풀이

# 입력
import sys
input = sys.stdin.readline
N = int(input())
xy_list = []
for _ in range(N):
    xy = list(map(int,input().split()))
    xy_list.append(xy)
sort_xy = sorted(xy_list)
print(sort_xy)
# # 2차원 배열 정렬
# # 먼저 x값만 비교하여 정렬 한다 
# restart = True
# while restart==True:
#     restart = False
#     for i in range(N-1):
#         if xy_list[i][0] > xy_list[i+1][0]:
#             xy_list[i],xy_list[i+1] = xy_list[i+1],xy_list[i]
#             restart = True            


# # x 값이 같을 때 뒤에 있는 y값이 더 크면 자리교환
# y_restart = True
# while y_restart == True:
#     y_restart = False
#     for i in range(N-1):
#             if xy_list[i][0] == xy_list[i+1][0]:
#                 if xy_list[i][1] > xy_list[i+1][1]:
#                     xy_list[i],xy_list[i+1] = xy_list[i+1],xy_list[i]
#                     y_restart = True
for i in sort_xy:
    result = " ".join(map(str,i))
    print(result)

# 와 sorted함수는 2차원 배열도 정렬해주네 이게 무슨...
# 난 왜 지금까지 저딴짓을...