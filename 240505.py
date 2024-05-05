#다이얼 5622
# 문제
# 상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.



# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

# 출력
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

#나의 풀이
dial = input()

#입력받은 문자를 숫자로 변환 하는 함수 생성 (2가지 형태)
def change(a):
    if a == 'A' or a =='B' or a =='C':
        return 2
    elif a == 'D' or a =='E' or a =='F':
        return 3
    elif a == 'G' or a =='H' or a =='I':
        return 4
    elif a == 'J' or a =='K' or a =='L':
        return 5
    elif a == 'M' or a =='N' or a =='O':
        return 6
    elif a == 'P' or a =='Q' or a =='R' or a == 'S':    
        return 7
    elif a == 'T' or a =='U' or a =='V':
        return 8
    elif a == 'W' or a =='X' or a =='Y' or a == 'Z':
        return 9
    
def change(a):
    if a == 'A':
        return 2
    elif a == 'B':
        return 2
    elif a == 'C':
        return 2
    elif a == 'D':
        return 3
    elif a == 'E':
        return 3
    elif a == 'F':
        return 3
    elif a == 'G':
        return 4
    elif a == 'H':
        return 4
    elif a == 'I':
        return 4
    elif a == 'J':
        return 5
    elif a == 'K':
        return 5
    elif a == 'L':
        return 5
    elif a == 'M':
        return 6
    elif a == 'N':
        return 6
    elif a == 'O':
        return 6
    elif a == 'P':
        return 7
    elif a == 'Q':
        return 7
    elif a == 'R':
        return 7
    elif a == 'S':
        return 7
    elif a == 'T':
        return 8
    elif a == 'U':
        return 8
    elif a == 'V':
        return 8
    elif a == 'W':
        return 9
    elif a == 'X':
        return 9
    elif a == 'Y':
        return 9
    elif a == 'Z':
        return 9
#계산부분
time = 0 # 전화를 걸기위한 최소 시간
for i in dial:
    time = time + (change(i)+1) #입력받은 문자를 번호로 변환후 해당 번호를 걸기위한 시간만큼 time에 더한다
print(time)


#다른 사람 풀이 
#리스트를 이용한 풀이이다
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input() 
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i: #만약 j가 dial의 i번째 인덱스값에 속한다면
            ret += dial.index(i)+3 #전체시간에 해당 다이얼의 인덱스에  +3
            #(+3인 이유는 해당 다이얼이 "ABC"라면 인덱스는 0이고 해당 값은 2 이다 
            #그러므로 인덱스와 값의 차는 2,
            #그리고 다이얼의 숫자와 입력 시간 은 1초 차이기 때문에 +1 해서 총 +3을 하게된다)
print(ret)
#=================================================================================================================
#그대로 출력하기 11718
# 문제
# 입력 받은 대로 출력하는 프로그램을 작성하시오.

# 입력
# 입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.

# 출력
# 입력받은 그대로 출력한다.

#나의 풀이
 
#다른 사람 풀이
while True:
    try:
        s = input()
        print(s)
    except EOFError:
        break
#try,except라는 것을 처음으로 배웠다
#try,except는 try에 있는 어떤 코드를 실행 할때 생기는 예외를 
#except 뒤에 적어 예외가 생각을때 작성한 코드를 실행하는 문법이다.
#예를 들면
try:
    number = int(input("숫자를 입력하세요: "))
    result = 2 / number
    print("결과:", result)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("올바른 숫자를 입력하세요.")
#위 처럼 입력받은 숫자를 2로 나눠 결과를 출력하는 코드에서 예외들 except뒤에 적고
#그 예외들이 발생 했을때 어떻게 대응 할것인지 아래 작성한다.

# 2번째 풀이 
import sys

words = sys.stdin.readlines()
for word in words:
    print(word.rstrip())
#두 번째 풀이는 sys,stdin의 readlines()를 활용한 방법이다
# readlines는 여러 입력을 한번에 바아 list로 return해주는 매서드이다.
# 각각의 문장의 마지막에는 개행문자('\n)가 함께 저장되므로 list에 접근하여 
#개별 원소를 출력할 때는 rstrip 매서드를 활용하여 개행문자를 제거해 줍니다.