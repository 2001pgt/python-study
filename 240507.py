#그룹 단어 체커 1316
# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

#나의 풀이

#단어 개수 입력
n = int(input())

group = n #처음은 전부 그룹단어라 가정하고 아닌단어를 찾을때마다 1씩 빼준다
for _ in range(n):
    s = input() #단어 입력
    for i in range(len(s)): 
        if i < len(s)-2 and len(s) > 2: #어쩌피 문자2개 이하는 그룹단어이므로 배제하고 인덱스 끝값과 그전 값도 달라도 상관없으므로 배제한다
            # 구현
            if s[i] != s[i+1]: #그룹단어가 되려면 aaabcca처럼 연결이 끝난 단어가 다시 뒤에서 재등장하면 안된다 그러므로 만약 연결이 끊어졌을때
                if s[i] in s[i+1:]: #i인덱스 값이 뒤에서 나타난다면(슬라이싱을 이용했다)
                    group -= 1 #그룹단어에서 해당 단어를 제외시킨다
                    break   #그리고 현재  for문을 탈출하고 다음 단어 판독
print(group)
#슬라이싱과if문을 활용하면 쉽게 풀수있는 문제인거 같다

#다른 사람 풀이
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1): 
        if word[j] == word[j+1]: #다음 단어가 같으면 pass
            pass
        elif word[j] in word[j+1:]: #다음 단어 이후에 j와 같은 단어가 있으면
            cnt -= 1 #카운트 -1
            break

print(cnt)
#내 코드 보다 간결하지만 풀이방식은 비슷한거같다.
#여기서도 슬라이싱과 if문을 잘 활용하여 풀었고 for문을 좀더 잘 다룬거 같다