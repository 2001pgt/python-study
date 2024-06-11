# 좌표 정렬하기2 11651
# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

# 풀이
# 어제 했던 문제와 유사하지만 y를 기준으로 정렬 하기 때문에
# reversed 함수를 통해서 x,y 좌표를 바꾼뒤 정렬 후 다시 reversed 함수로 바꿔 출력한다.
import sys
input = sys.stdin.readline
# 입력
N = int(input()) 
# 빈리스트 생성
xy_list = []
# x,y를 입력후 리버스 후 리스트 삽입
for _ in range(N):
    xy = list(map(int,input().split()))
    xy = list(reversed(xy))
    xy_list.append(xy)
# y,x 상태를 정렬
sort_xy = sorted(xy_list)

for i in sort_xy:
    # 다시 리버스 후 출력
    result = " ".join(map(str,reversed(i)))
    print(result)