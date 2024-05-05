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

#단어 공부 1157 
# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
#나의 풀이
word = input() # 단어 입력
word = word.lower() # 단어를 전부 소문자로 변경
word = list(word) #리스트로 형태 변환
#각각의 알파벳의 입력횟수
total_a = 0
total_b = 0
total_c = 0
total_d = 0
total_e = 0
total_f = 0
total_g = 0
total_h = 0
total_i = 0
total_j = 0
total_k = 0
total_l = 0
total_m = 0
total_n = 0
total_o = 0
total_p = 0
total_q = 0
total_r = 0
total_s = 0
total_t = 0
total_u = 0
total_v = 0
total_w = 0
total_x = 0
total_y = 0
total_z = 0
#해당 알파벳이 입력될때마다 카운트+1
for i in word:
    if i == 'a':
        total_a += 1
    elif i == 'b':
        total_b += 1
    elif i == 'c':
        total_c += 1
    elif i == 'd':
        total_d += 1
    elif i == 'e':
        total_e += 1
    elif i == 'f':
        total_f += 1
    elif i == 'g':
        total_g += 1
    elif i == 'h':
        total_h += 1
    elif i == 'i':
        total_i += 1
    elif i == 'j':
        total_j += 1
    elif i == 'k':
        total_k += 1
    elif i == 'l':
        total_l += 1
    elif i == 'm':
        total_m += 1
    elif i == 'n':
        total_n += 1
    elif i == 'o':
        total_o += 1
    elif i == 'p':
        total_p += 1
    elif i == 'q':
        total_q += 1
    elif i == 'r':
        total_r += 1
    elif i == 's':
        total_s += 1
    elif i == 't':
        total_t += 1
    elif i == 'u':
        total_u += 1
    elif i == 'v':
        total_v += 1
    elif i == 'w':
        total_w += 1
    elif i == 'x':
        total_x += 1
    elif i == 'y':
        total_y += 1
    elif i == 'z':
        total_z += 1
#각 알파벳 카운트들을 리스트에 저장후 크기순 정렬
my_list = []
my_list.append(total_a)
my_list.append(total_b)
my_list.append(total_c)
my_list.append(total_d)
my_list.append(total_e)
my_list.append(total_f)
my_list.append(total_g)
my_list.append(total_h)
my_list.append(total_i)
my_list.append(total_j)
my_list.append(total_k)
my_list.append(total_l)
my_list.append(total_m)
my_list.append(total_n)
my_list.append(total_o)
my_list.append(total_p)
my_list.append(total_q)
my_list.append(total_r)
my_list.append(total_s)
my_list.append(total_t)
my_list.append(total_u)
my_list.append(total_v)
my_list.append(total_w)
my_list.append(total_x)
my_list.append(total_y)
my_list.append(total_z)
sort_word = my_list.sort() #정보) sort()매서드는 리스트를 정렬하고 리턴값으로 None을 리턴하기 때문에 단순히 정렬만 하고싶다면 sorted(리스트)함수를 써도 된다
#가장 큰 카운트를 찾는다
max_word = max(my_list)
#단어가 1글자 일때는 해당 단어를 대문자로 출력
if len(word) == 1:
    word = ''.join(word)
    s = word.upper()
    print(s)
#카운트가 같은 알파벳이 있을경우 ?출력
elif my_list[len(my_list)-1] == my_list[len(my_list)-2]:
    print('?')
#가장 큰 카운터를 가진 알파벳을 대문자로 출력한다
elif max_word == total_a :
    print('A')
elif max_word == total_b :
    print('B')
elif max_word == total_c :
    print('C')
elif max_word == total_d :
    print('D')
elif max_word == total_e :
    print('E')
elif max_word == total_f :
    print('F')
elif max_word == total_g :
    print('G')
elif max_word == total_h :
    print('H')
elif max_word == total_i :
    print('I')
elif max_word == total_j :
    print('J')
elif max_word == total_k :
    print('K')
elif max_word == total_l :
    print('L')
elif max_word == total_m :
    print('M')
elif max_word == total_n :
    print('N')
elif max_word == total_o :
    print('O')
elif max_word == total_p :
    print('P')
elif max_word == total_q :
    print('Q')
elif max_word == total_r :
    print('R')
elif max_word == total_s :
    print('S')
elif max_word == total_t :
    print('T')
elif max_word == total_u :
    print('U')
elif max_word == total_v :
    print('V')
elif max_word == total_w :
    print('W')
elif max_word == total_x :
    print('X')
elif max_word == total_y :
    print('Y')
elif max_word == total_z :
    print('Z')
# 생각보다 너무 노가다만 한거같네...

#다른 사람 풀이
# upper 메소드를 사용하여 전체 문자를 대문자로 변환하여 변수에 저장한다.
# 비교를 하기 위해 set함수를 사용하여 중복된 문자값을 제거한 후 변수에 저장한다.
# for문을 이용하여 알파벳이 사용된 횟수를 리스트에 저장한다.
# if 문을 사용하여 출력문을 작성하고, 알파벳이 사용된 갯주 중 1보다 크면 물음표를 출력하게 한다.
# 최대값이 하나라면 숫자 리스트 중에서 가장 큰 수의 위치를 index로 찾아 인덱스에 위치한 문자열을 출력한다.
word = input().upper()
word_list = list(set(word))#set() 함수는 파이썬 내장 함수 중 하나로, 주어진 시퀀스(리스트, 튜플 등)나 다른 반복 가능한 객체에서 중복된 요소를 제거하고 유일한 요소들로 이루어진 집합(set)을 생성합니다.
#set()함수 예시
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print(unique_set)  # 출력: {1, 2, 3, 4, 5}
#==========================================
cnt = []
for i in word_list:
  count = word.count #count() 함수는 리스트, 튜플, 문자열 등의 시퀀스에서 특정 요소의 등장 횟수를 세는 파이썬 내장 함수입니다. 이 함수는 주어진 요소의 등장 횟수를 반환합니다.
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:#가장 큰 카운트가 여러개 1보다 크다면
  print("?") #? 출력

else: #아니면
  print(word_list[(cnt.index(max(cnt)))]) #숫자 리스트 중에서 가장 큰 수의 위치를 index로 찾아 인덱스에 위치한 문자열을 출력한다.
#   upper메소드의 사용법 대하여 알 수 있었다.
# count메소드의 사용법에 대해 알 수 있었다.
# index, max 함수에 대해 알 수 있었다.
#count 예시
my_list = [1, 2, 2, 3, 3, 3, 4, 5]
count_of_3 = my_list.count(3)
print(count_of_3)  # 출력: 3