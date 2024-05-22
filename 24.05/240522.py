#약수 구하기 2501
# 문제
# 어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다. 

# 6을 예로 들면

# 6 ÷ 1 = 6 … 0
# 6 ÷ 2 = 3 … 0
# 6 ÷ 3 = 2 … 0
# 6 ÷ 4 = 1 … 2
# 6 ÷ 5 = 1 … 1
# 6 ÷ 6 = 1 … 0
# 그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.

# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.

# 출력
# 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.

#나의 풀이
#N,K입력받기
N , K = map(int,input().split())

# N의 약수 중 K번째로 작은수 찾기

# N의 약수들을 먼저 찾아낸다. -> N의 약수들을 빈리스트안에 추가하여 골라낸다

div_list = []
for i in range(1,N+1):
    if N % i == 0:
        div_list.append(i)
#약수는 작은 수 부터 차례대로 저장된다.

# 골라낸 약수중 인덱싱을 이용하여 k번째로 작은 수를 찾는다.
try:
    print(div_list[K-1])
except IndexError:
    print(0)

#다른 풀이
arr=[]
N, K = map(int, input().split())
cnt = 0
for i in range(1, N + 1):
    if N % i == 0:
        arr.append(i)
    cnt += 1

if K > len(arr):
    print(0)
else:
    print(arr[K-1])
# 마지막에 출력 부분에서 k값이 약수의 개수 범위 외 일때
# 나는 try except를 써서 처리했지만
# 이 풀이는 if문으로 K값이 약수 리스트 개수 보다 크면 0을 출력하도록 하였다

#약수들의 합 9506
# 문제
# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.

# 예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.

# n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

# 입력
# 입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100,000)

# 입력의 마지막엔 -1이 주어진다.

# 출력
# 테스트케이스 마다 한줄에 하나씩 출력해야 한다.

# n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).

# 이때, 약수들은 오름차순으로 나열해야 한다.

# n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.

#나의 풀이

while True:
    # n 입력
    n = int(input())
    # n = -1 일때 입력종료
    if n == -1:
        break  
    # n이 완전수 인지 확인

    # n이 완전수 이기 위해서 자신을 제외한 약수들의 합이 n과 같아야한다. 

    # 먼저 n 의 약수들을 뽑아낸다.
    div_list = []
    for i in range(1,n):
        if n % i == 0:
            div_list.append(i)
    # 약수들의 합을 확인 한다.
    hap = sum(div_list)
    #hap과 n이 같은지 확인
    if n == hap:
        #map ,join함수를 이용해서 약수들의 합을 문자열로 표현
        print(f'{n} = {" + ".join(map(str,div_list))}')
    else:
        print(f'{n} is NOT perfect.')


#다른 풀이
while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        print(n, "=", end=" ")
        print(*arr, sep=" + ")
    else:
        print(n, "is NOT perfect.")

#풀이2
while True:
    n = int(input())
    if n == -1: # 입력 값이 -1이면 반복문 종료
        break
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")
    else:
        print(n, "is NOT perfect.")
#두 풀이다 출력부분을 제외한 나머지는 같다
#첫번째 풀이는 join을 활용하지 않고 sep=만을 활용하여 리스트 안의 인자들을 + 를 사이에 두고 출력되게 만들었다.
# 두번째 풀이는 join을 활용한 것은 같았지만 sep= 또한 활용하여 ,을 사용했을때 발생하는 불피요한 공백들을 제거하였다.

# 소수 찾기 1978
# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

# 나의 풀이
# N 을 입력받고 N개 만큼 숫자 입력받기
N = int(input())
nums = list(map(int,input().split()))

# 입력받은 수들 중에서 소수 찾기
# 소수의 조건 1보다 크고, 약수가 본인과 1만 있어야 한다.
# 확인 방법 2~(n-1) 까지 수들 전부 나눴때 나머지가 0이 되는 수가 없는지 확인
# 입력받은 숫자들을 하나씩 확인
cnt = N
for i in nums:
    # 1은 소수가 아니기 때문에 제외
    if i == 1:
        cnt -= 1
    # 2는 소수이므로 넘기고 3이상 일때부터 확인시작
    elif i > 2:
        # 2 ~ 본인 제외 숫자 까지중에
        for i2 in range(2,i-1):
            # 소수가 아남이 증명되면
            if i % i2 == 0:
                #카운트 제거
                cnt -= 1
                break # 중복제거 방지를 위함
print(cnt)

#다른 풀이
#특별히 좋은 풀이가 보이지않아 생략