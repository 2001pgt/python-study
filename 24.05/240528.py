# 삼각형과 세 변 5073
# 문제
# 삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.

# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# 단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다. 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.

# 세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.

# 입력
# 각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.

# 출력
# 각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.

# 풀이

while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    # 삼각형의 조건을 만족 할 때
    if a + b >c and a+c > b and b+c >a:
         # 세 변이 전부 같을 때
        if a == b == c:
            print('Equilateral')
        # 두 변만 같은 경우
        elif a == b !=c or b==c!=a or c==a!=b:
            print('Isosceles')
        # 세 변이 전부 다를 때
        elif a != b != c:
            print('Scalene')
    # 삼각형의 조건을 만족하지 못했을때
    else:
        print('Invalid')

# 다른 풀이
while 1:
    li = sorted(list(map(int, input().split())))
    if li[0] == li[1] == li[2] == 0:
        break
    if li[0]+li[1] <= li[2]:
        print("Invalid")
    elif li[0] == li[1] == li[2]:
        print("Equilateral")
    elif li[0]==li[1] or li[1]==li[2] or li[2]==li[0]:
        print("Isosceles")
    else:
        print("Scalene")
    
    # 리스트 정렬을 활용하여 삼각형의 각변의 크기의 순서를 알아낸뒤
    # 삼각형 가장 큰변의 길이가 나머지 두변의 길이의 합보다 작다는 조건을 아주 쉽게 구현했다
    