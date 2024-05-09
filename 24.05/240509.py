# 행렬 덧셈 2738
# 문제
# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

# 출력
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

#나의 풀이
N,M = map(int,(input().split()))#N가로 ,M세로
# 행렬2개를 만들기위한 빈 리스트2개 생성
matrix1 = []
matrix2 = []
#리스트에 행렬2개 입력 추가
for _ in range(N):
    sum_list1 = list(map(int,input().split()))
    matrix1.append(sum_list1)
for _ in range(N):
    sum_list2 = list(map(int,input().split()))
    matrix2.append(sum_list2)

#두 행렬의 각 원소들을 더하여 새로운 리스트에 추가
new_matrix = []
for i in range(N):
    for i2 in range(M):
        new_matrix.append(matrix1[i][i2]+matrix2[i][i2])

#출력
for i in range(M*N):
    if i % M == 0:
        print()
        print(new_matrix[i],end=' ')
    else:
        print(new_matrix[i],end=' ')
#예제를 출력했을 때 정답이 나오지만 막상 풀이를 제출하니
#"출력형식이 잘못되었습니다"라고 뜬다. 그래서 다른 사람의 풀이를 봤더니 나와 같으나 마지막 출력부분이 달라 그것을 참고하여 다시 풀이를 써보았다.
#나의 풀이(수정)
N,M = map(int,(input().split()))#N가로 ,M세로
matrix1 = []
matrix2 = []
for _ in range(N):
    sum_list1 = list(map(int,input().split()))
    matrix1.append(sum_list1)
for _ in range(N):
    sum_list2 = list(map(int,input().split()))
    matrix2.append(sum_list2)

for row in range(N):
    for col in range(M):
        print(matrix1[row][col] + matrix2[row][col], end=' ')
    print()


#다른 사람 풀이
A, B = [], []

N, M = map(int, input().split())

for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)
#여기까지는 나와 같고

#여기부터는 각각의 행렬의 원소를 바로 더하여 출력하였다.
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()
