# 수 정렬하기 2751
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

#풀이

# 입력
N = int(input())
# 입력받은 수를 저장하는 리스트
# 리스트 컴프리헨션
num = [int(input()) for _ in range(N)]
new_num = sorted(num)
# 삽입정렬을 활용해 오름차순 정렬
# def insertion_sort(A):
#     for i in range(1, len(A)):
#         key = A[i]
#         j = i - 1
#         while j >= 0 and key < A[j]:
#             A[j + 1] = A[j]
#             j -= 1
#         A[j + 1] = key
#     return A
# insertion_sort(num)

for i in new_num:
    print(i)