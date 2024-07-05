# 서로 다른 부분 문자열의 개수 11478
# 문제
# 문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.

# 부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.

# 예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.

# 입력
# 첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.

# 출력
# 첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.

# 풀이
# 입력
# import sys
# input = sys.stdin.readline
# S = list(input().strip())
# # 빈리스트 생성
# some_str = []
# # 입력받은 문자열의 부분 문자열을 모두 생성하여 빈리스트에 추가
# for i in range(len(S)):
#     for x in range(i+1,len(S)+1):
#             # 추가할 때 join함수를 이용하여 []를 제거하고 문자열의 형태로 넣는다
#             some_str.append(''.join(S[i:x]))
# # 그리고  set 으로 변환하여 중복제거 후 list로 돌아와서 개수를 샌다
# some_str = set(some_str)
# some_str = list(some_str)
# print(len(some_str))

# 다른 풀이

# 처음부터 리스트로 문자열을 입력 받아버려서 풀이가 꼬여버렸다.
# 빈 set()에 슬라이싱한 문자열을 넣으려는데 안되서 왜 안되지? 했는데 리스트형태로 set에 넣으려고 해서 안되는것였다.
# 그래서 그냥 문자열로 입력 받은 경우로 풀어보겠다.
S = input()

cnt = set()

data_length = len(S)

for i in range(data_length):
    for j in range(i+1, data_length+1):
        cnt.add(S[i:j])

print(len(cnt))
# 풀이는 거의 똑같고 리스트 대신 세트를 사용한다