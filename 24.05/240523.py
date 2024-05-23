#소수 2581
# 문제
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 입력
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

# 출력
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

#나의 풀이

M = int(input())
N = int(input())

# 소수의 조건 1보다 크고, 약수가 본인과 1만 있어야 한다.
# 확인 방법 2~(n-1) 까지 수들 전부 나눴때 나머지가 0이 되는 수가 없는지 확인

#빈 소수 리스트 생성
sosu = []
# M~N까지 소수 검사
for num in range(M,N+1):
    # 소수 추가를 위한 세팅
    s_break = False
    # num = 1 일때 스킵
    if num == 1:
        continue
    # num = 2 일때 리스트에 추가
    elif num == 2:
        sosu.append(num)
    # 소수를 판단할때는 2부터 나눠봐야하기 때문에 2부터 시작
    elif num > 2:
        for i in range(2,num): 
            # num 이 i 로 나누어 떨어지면 소수가 아니다
            if num % i == 0:
                #소수가 아닐때 
                s_break = True
                break #멈추고 다음수 검사 시작
        # 소수가 아니면 바로 다음 숫자로 넘어가기 위한 장치
        if s_break == True:
            continue
        # 아무일도 일어나지 않고 통과할시
        # 해당 num을 리스트에 저장
        sosu.append(num)

if len(sosu) >= 1:
    print(sum(sosu))  
    print(sosu[0])
else:
    print(-1)

#다른 풀이
M = int(input())
N = int(input())

sosu_list = []
for num in range(M, N+1): # M이상 ~ N이하의 수
    count = 0 # 나눠지는 수가 있으면 카운트
    if num > 1: # 2이상의 수들 중에 소수를 찾는다.
        for i in range(2, num): # 2~num에서 나눠지는 수를 찾는다
            if num % i == 0: # 나머지가 0이면 나눠지는 수(소수 아님)
                count += 1 # 소수가 아님을 카운트
                break
        if count == 0: # 나눠지는 수가 없으면 소수
            sosu_list.append(num)


if len(sosu_list) > 0:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)

# 이 문제의 핵심은 소수가라고 판정됐을때 어떻게 소수를 오류없이 리스트에 추가하는냐가 핵심이다 그래서 대부분 특정 조건을 걸고 그 조건에 부합하면 소수를 리스트에 추가하는 방식을 택했다.