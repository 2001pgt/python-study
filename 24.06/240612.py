# 단어 정렬 1181
# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다.

# 풀이

# 입력
import sys
input = sys.stdin.readline
N = int(input().strip())
words = []
for _ in range(N):
    word = input().strip()
    words.append(word)
# 중복 제거
words = list(set(words))
# 단어 길이에 따라 정렬
restart = True
while restart:
    restart = False
    for i in range(len(words)-1):
        if len(words[i]) > len(words[i+1]):
            words[i],words[i+1] = words[i+1],words[i]
            restart = True
# 사전 순서에 따라 길이가 같은 단어 재정렬
for _ in range(len(words)):
    for i in range(len(words)-1):
        if len(words[i]) == len(words[i+1]):
            subset = words[i:i+2]
            subset.sort()
            words[i:i+2] = subset
for i in words:
    print(i)
# 이렇게 풀면 정답은 나오지만 풀이 제출시 시간초과로 인해
# 오답이라고 뜬다

# 다른풀이
# 이 풀이는 sort()메소드를 활용하여 간단하게 풀이를 하였다
n = int(input())
lst = []

for i in range(n):
    lst.append(input())

lst.sort()	## 괄호 안에 아무 값도 넣지 않으면 알파벳 순서대로 정렬을 해 준다.
lst.sort(key = len)	## 문자열 길이 순으로 정렬.

for i in lst:
    print(i)
# 두번째sys.stdin.readline() 활용 
n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)
# sort() 메소드는 생각보다 엄청 활용도가 높은 함수였다.
# 처음 길이에 따라 정렬을 할때 우선순위 큐를 활용해 길이를 key로 두고 key의 우선순위에 따라 정렬 해야되나 생각했지만 아직 자료구조를 완전히 다룰줄 몰라 위의 풀이처럼 진해하였다.
# 하지만 sort()메서드 에서 sort(key)를 활용하면 다양한 조건을 걸어서 정렬이 가능하였다.