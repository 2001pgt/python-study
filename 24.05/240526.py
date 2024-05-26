#네번째점 3009
# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

#풀이

#1000x1000좌표계 생성

#직사각형의 성질에 의하면
# x4 = x1 ,x2, x3 중 더 적게 나온 숫자이다
# y4도 마찬가지

#점 세개 입력
x_list=[]
y_list=[]
for _ in range(3):
    x,y=map(int,input().split())
    # x,y좌표를 각 리스트에 추가
    x_list.append(x)
    y_list.append(y)
# 빈도수가 가장 작은 수를 추출
# 리스트에서 두 숫자를 세서 더작은수를출력

max_x = max(x_list)
min_x = min(x_list)
cnt_max_x = x_list.count(max_x)
cnt_min_x = x_list.count(min_x)

if cnt_max_x > cnt_min_x:
    my_x = min_x
else:
    my_x = max_x

max_y = max(y_list)
min_y = min(y_list)
cnt_max_y = y_list.count(max_y)
cnt_min_y = y_list.count(min_y)

if cnt_max_y > cnt_min_y:
    my_y = min_y
else:
    my_y = max_y
print(my_x,my_y)

#다른 풀이
x_points = []
y_points = []

for _ in range(3):
    x, y = map(int, input().split())
    x_points.append(x)
    y_points.append(y)

for i in range(3):
    if x_points.count(x_points[i]) == 1:
        x4 = x_points[i]
    if y_points.count(y_points[i]) == 1:
        y4 = y_points[i]

print(x4, y4)

#이 풀이는 x,y의 출현횟수를 찾을때for문을 활용하여 더 간단히 구현하였다.
#하지만실행시간은 108ms으로 같았다.