#색종이 2563
# 문제
# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.



# 예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다.

# 입력
# 첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다

# 출력
# 첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.

#나의풀이
n = int(input())
cnt = 0
black = []

#검은 색종이 생성
for _ in range(n):
    x,y = map(int,input().split()) #검은 색종이 좌표 입력
    new_black = []
    for i in range(y,y+11):
        for i2 in range(x,x+11):
            new_black.append([i2,i]) #새로운 색종이의 좌표를 리스트로 만들어 다시 새로운 색종이 리스트에 추가
    black.append(new_black)    
print(black)
    #두개의 색종이를 비교해서 겹치는 좌표들을 리스트에 넣어 가장 x,y값이 작은 좌표와 큰좌표를 찾아 넓이를 구한다.
#in 함수를 사용해 두 색종이 겹치는 부분을 확인한다.
stack_black = []
for i in range(n):
    for i2 in range(len(black[0])):
        if i < n-1:
            if black[i][i2] in black[i+1]:
                stack_black.append(black[i][i2])
    print(stack_black)
    mini_x = 100000
    mini_y = 100000
    max_x = 0
    max_y = 0
    ghup = []
    total = 0
    for i in range(len(stack_black)):
        for i2 in range(2):
            if i < len(black)-1:
                if ((black[i][0])**2 + (black[i][1])**2) < ((mini_x)**2 + (mini_y)**2):
                    mini_x = black[i][0]
                    mini_y = black[i][1]
                if ((black[i][0])**2 + (black[i][1])**2) > ((max_x)**2 + (max_y)**2):
                    max_x = black[i][0]
                    max_y = black[i][1]
    #각각의 최소최대좌표를 이용해 겹치는 구역의 넣이를 구하고 그것을 다시 리스트에 저장한다.
    area = (max_x-mini_x)*(max_y-mini_y)
    ghup.append(area)
    total += area        
print(total)
#나는 바보다...
#나는 각 검은종이가 겹치는 좌표들을 구해 넓이를 더하려고 했다
#하지만 그렇게하면 너무 많은 경우의 수에 대비하려 할때 코드가 매우 복잡해진다.
#그래서 결국 포기하고 다른 사람의 풀이를 보니 내풀이가 완전히 잘못 되었음을 깨달았다.

#다른사람풀이
N = int(input())
array = [[0] * 100 for _ in range(100)]  # 도화지 범위 초기화
for _ in range(N):  # 입력 받은 도화지 개수만큼 돈다.
    y1, x1 = map(int, input().split())  # 왼쪽아래 x,y 좌표를 받는다.

    for i in range(x1, x1 + 10):  # 세로를 돈다.
        for j in range(y1, y1 + 10):  # 가로를 돈다.
            array[i][j] = 1  # 해당 범위 값을 0에서 1로 바꿔준다.

result = 0  # 넓이를 출력할 변수
for k in range(100):  # 전체 도화지를 돌면서
    result += array[k].count(1)  # 1 개수만 세어준다

print(result)

#이 풀이는 전체 100X100개의 각좌표에 0을넣고 검은 색종이가 덮는 부분은 1로 바꿔주는 기가막힌 풀이를 보여준다.
#이풀이를 보고 나는 아직 갈길 많이 멀었구나 느꼈다.