# 수 정렬하기3 10989
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 풀이
import sys
input = sys.stdin.readline
# 입력
N = int(input())
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 리스트의 끝에 새 노드 추가
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # 리스트 출력
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

    # 리스트의 특정 위치에 새 노드 삽입
    def insert(self, prev_node, data):
        if not prev_node:
            print("이전 노드가 존재하지 않습니다.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # 리스트에서 특정 데이터 삭제
    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None
# 계수 정렬
def optimized_counting_sort(arr):
    if not arr:
        return arr
    
    # 입력 배열에서 최대값과 최소값을 구함
    min_val = min(arr)
    max_val = max(arr)
    
    # 입력 배열의 범위에 맞는 카운트 배열을 생성
    range_of_elements = max_val - min_val + 1
    count_arr = [0] * range_of_elements
    
    # 입력 배열의 각 요소에 대한 카운트 증가
    for num in arr:
        count_arr[num - min_val] += 1
    
    # 누적 합 계산 및 바로 입력 배열에 적용하여 정렬
    sorted_index = 0
    for i in range(range_of_elements):
        while count_arr[i] > 0:
            arr[sorted_index] = i + min_val
            sorted_index += 1
            count_arr[i] -= 1
    
    return arr
num = LinkedList()
for _ in range(N):
    num.append(int(input()))


sorted_arr = optimized_counting_sort(num)
for i in sorted_arr:
    print(i)
# 정답import sys
input = sys.stdin.readline

#계수정렬 활용
n = int(input())
arr = [0] * (10000 + 1) # 입력값이 10000개까지 주어지니 10000 + 1개의 리스트 선언

#각 입력값에 해당하는 인덱스의 값 증가
for _ in range(n):
    arr[int(input())] += 1
  
#arr에 기록된 정보 확인
for i in range(len(arr)):
    if arr[i] != 0: #0이 아닌 데이터, 즉 입력받은 데이터들을 출력
        for _ in range(arr[i]):
            print(i)
# 해당문제는 메모리 초과를 해결하는 것이 가장 중요하다
# 이를 위해 sort 함수대신 계수정렬, input 대신 int(sys.stdin.readline())를 사용하는 것이 핵심이다.