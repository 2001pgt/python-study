#벌집
# 문제


# 위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

# 출력
# 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

#나의 풀이
#첫줄은 1개
#둘째줄은6개
#셋째줄은17개씩 들어간다
#그러므로 n번째 줄의 개수는 (6xn)+(n-1번째줄의개수)라는 규칙이 나온다
#이를 이용하여 코드를 짜면
N = int(input())
bucket = 1 #총 숫자의 개수
cnt = 1 #6각형을 돌면서 숫자를 채우는 바퀴수

while N > bucket:
    bucket += 6 * cnt #현재 총 수자 개수 위의 식을 활용
    cnt += 1
print(cnt)