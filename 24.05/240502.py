#단어 공부 1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

#나의 풀이
a = input()
word = a.lower()

#문자 i와 나머지 문자들을 모두 비교하여 같은 것이 나올 때마다count+1을 한다 이렇게 모든 문자들을 비교하여 count가 가장 높은 문자를 출력하게 한다
word_count = 0
max_count = 0
for i in range(len(word)):
    for i2 in range(len(word)):
        if word[i] == word[i2]:
            word_count += 1
    if max_count < word_count:
        max_count = word_count
    
    