today="화요일"#요일
if today=='일요일':
    print("게임")
print('공부')
#elif는 아니라고? 그럼 이건 어때? 라는 뜻

#if중첩
yellow_card=1
foul=True
if foul:
    yellow_card+=1
    if yellow_card==2:
        print('레드카드')
    else:
        print("살았다")
else:
    print('주의')


#for 반복문
#for변수 in 반복 범위 또는 대상:
    #ㄴ반복문 실행 문법

for num in range(1,5):#range 안에서 (1,5)는 1부터 5미만의 숫자를 순서대로 반복하라는 뜻이다 
    print(f'당신의 번호는{num}번 입니다')#1~4까지 순서대로 반복
    print(num)
#for num2 in range(start,stop,step) #step은 start와stop사이의 숫자를 반복할때 step값 만큼 띄어서 반복한다
#예시
for num1 in range(1,11,2):#홀수만 반복
    print(num1)
print('for활용 시작')
#for 활용
#리스트,튜플,딕셔너리등 문자열 자료를 이용하여 for를 사용 할 수 있다
my_list=[1,2,3,4,5,6,7]
for num2 in my_list:
    print(num2)
print('튜플 활용')#튜플 활용
my_tuple=(5,4,3,2,1)
for num3 in my_tuple:
    print(num3)
print('딕셔너리 활용')#딕셔너리 활용
student={'학번':'20','학과':'컴공','이름':'박'}#딕셔너리 선언
for x in student.keys():#key만 뽑아서 정렬
    print(x)
for y in student.values():#value만 뽑아서 정렬
    print(y)
for k,v in student.items():#둘 다 뽑아서 정렬,이 때 for뒤에는 key와value둘 다 뽑기위해 2개의 변수를 사용한다
    print(k,v)#여기도 위와 마찬가지
    





















