# 문자열 집합 14425

# 문제
# 총 N개의 문자열로 이루어진 집합 S가 주어진다.

# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다. 

# 다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.

# 다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

# 입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

# 출력
# 첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.

# 풀이

# 입력
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

# 집합 S 입력
S = []
for i in range(N):
    S.append(input())

# M개의 문자열 입력
result = 0
for i in range(M):
    if input() in S: # S안에 있으면
        result += 1 # 결과값을 +1
    if result == N:
        break
print(result)
# 이 풀이는 코드를 읽기 편하지만 시간초과가 뜬다

# 그래서 검색 속도를 빠르게 하기위해 딕셔너리를 활용해 보았다.
result = 0 
dict ={}
# 빈 딕셔너리에 문자를 추가 value 값은 0으로 고정
for i in range(N):
    dict[input()] = 0
# 같은 문자가 입력되면 result +1
for i in range(M):
    if input() in dict:
        result += 1
print(result)
# 리스트는 검색 시간복잡도가 O(N)이 걸리지만 해시테이블을 사용하는 딕셔너리와 세트는  O(1) 의 시간 복잡도를 가지므로 
# 검색시간이 상수시간으로 단축된다
# 아직 해시 테이블에 대해서 배우지 않아 자세히는 모르지만 검색을 하기위한 자료구조인거 같다

# 다른 풀이
# 그리고 다른 풀이를 보니 set을 사용 했던데 딕셔너리와 다르게 key값만 가지고 순서와 중복이 없는 set이 이문제에 더 적합한거 같다
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

# 빈 세트 생성
my_set = set()
# 문자 추가
for _ in range(N):
    my_set.add(input())

# 입력된 문자와 비교
result = 0 
for i in range(M):
    if input() in my_set:
        result += 1
print(result)

# 추가 적인 set 설명
# 빈 set 생성
my_set = set()

# 초기 값이 있는 set 생성
my_set = {1, 2, 3, 4}

my_set = {1, 2, 3}

# 요소 추가
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# 요소 제거
my_set.remove(2)
print(my_set)  # {1, 3, 4}

# 존재하지 않는 요소 제거 시 KeyError 발생
# my_set.remove(5)  # KeyError

# 존재하지 않는 요소 제거 시 에러 방지
my_set.discard(5)  # 에러 없음
print(my_set)  # {1, 3, 4}

# 모든 요소 제거
my_set.clear()
print(my_set)  # set()

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 합집합
union_set = set1 | set2
print(union_set)  # {1, 2, 3, 4, 5}

# 교집합
intersection_set = set1 & set2
print(intersection_set)  # {3}

# 차집합
difference_set = set1 - set2
print(difference_set)  # {1, 2}

# 대칭 차집합
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # {1, 2, 4, 5}

my_set = {1, 2, 3}

# 요소 존재 여부 확인
print(2 in my_set)  # True
print(4 in my_set)  # False

my_set = {1, 2, 3}

for element in my_set:
    print(element)
# 출력 순서는 정해져 있지 않음

# 예제: 두 리스트에서 중복되지 않은 요소 찾기
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

unique_elements = set1 ^ set2
print(unique_elements)  # {1, 2, 3, 6, 7, 8}
