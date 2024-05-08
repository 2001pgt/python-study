#문자열 반복 2675
# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

#나의 풀이
T = int(input()) #테스트 횟수 입력

test = 0
#abc 는 aaabbbccc
while test < T: #test
    R,S = input().split() #R과S를 공백으로 구분하여 입력
    R = int(R) #R은 반복 횟수이므로 정수로 변환
    for i in range(len(S)):
        #마지막 문자 일때
        if i == len(S)-1: 
            print(S[i]*R) #줄 바꿈을 위해 end='' 사용 X
        #나머지 문자들
        else:        
            print(S[i]*R,end='') #줄바꿈X
    test += 1 #테스트 1회 때마다 횟수 +1

#다른 사람의 풀이
Case = int(input()) #테스트 횟수

for i in range(Case): #테스트 횟수 case번 동안
    N, S = input().split() #N과S를 입력받고 
    for j in range(len(S)): 
        print(S[j] * int(N), end = '') #이사람은 나와 다르게 줄바꿈을 여기서 따로 하지 않고
    print('')# 마지막에 추가로 줄바꿈을 위해 print()문을 추가로 입력하였다.
