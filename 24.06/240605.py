# 정렬
# 선택 정렬
# 최대 원소 찾기
def Largest(A,last):
    max_num = A[0]
    max_index = 0
    for i in range(last+1):
        if a[i] > max_num:
            max_num = a[i] 
            max_index = i
    return max_index
# 최대 원소와 맨 오른쪽 자리 바꾸기 
def SelectionSort(A):
    # 가장 큰 원소의 인덱스
    for last in range(len(A)-1,0,-1):
        max_index = Largest(A,last)
        A[max_index],A[last] = A[last] , A[max_index]

# 수 정렬하기(선택정렬) 2750
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
# 풀이
a = []
# N 입력
N = int(input())
# 숫자 입력
for _ in range(N):
    a.append(int(input()))

# 선택 정렬
SelectionSort(a)
# 출력
for i in a:
    print(i)

# 대표값2 2587
# 문제
# 어떤 수들이 있을 때, 그 수들을 대표하는 값으로 가장 흔하게 쓰이는 것은 평균이다. 평균은 주어진 모든 수의 합을 수의 개수로 나눈 것이다. 예를 들어 10, 40, 30, 60, 30의 평균은 (10 + 40 + 30 + 60 + 30) / 5 = 170 / 5 = 34가 된다.

# 평균 이외의 또 다른 대표값으로 중앙값이라는 것이 있다. 중앙값은 주어진 수를 크기 순서대로 늘어 놓았을 때 가장 중앙에 놓인 값이다. 예를 들어 10, 40, 30, 60, 30의 경우, 크기 순서대로 늘어 놓으면

# 10 30 30 40 60

# 이 되고 따라서 중앙값은 30이 된다.

# 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄부터 다섯 번째 줄까지 한 줄에 하나씩 자연수가 주어진다. 주어지는 자연수는 100 보다 작은 10의 배수이다.

# 출력
# 첫째 줄에는 평균을 출력하고, 둘째 줄에는 중앙값을 출력한다. 평균과 중앙값은 모두 자연수이다.

# 풀이 
# 이 문제는 자료구조 시간에 배운 버블 정렬을 활용해서 풀어보도록 하겠다.

# 버블 정렬 
def bubbleSort(A):
    # 처음부터 한칸씩 이동하면서 두 원소가 순서대로 되어 있지 않으면 자리를 변경
    # 순회 할때마다 정렬된 원소들을 제외
    for lenght in range(len(A)-1,0,-1):
        # 남은 원소들 중 가장 큰 값 찾기
        for i in range(lenght):
                # 맨 처음 값부터
                if A[i] > A[i+1]:
                    A[i] , A[i+1] = A[i+1] , A[i]
a = []
for _ in range(5):
    a.append(int(input()))
bubbleSort(a)
# 평균값
print(sum(a)//5)
# 중앙값
print(a[2])