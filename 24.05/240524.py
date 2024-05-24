#소인수분해 11653   
# 문제
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

# 출력
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

#풀이

# N 입력
N = int(input())
#소인수는 약수이면서 소수 이어야한다.

# 소인수분해 시작
soinsu = []
while True:
    if N == 1:
        break
    elif N == 2:
        print(2)
        break
    # 멈춤 조건 -> 더이상 N을 소인수분해 할 수 없을때 
    # 기본 멈춤값 설정
    stop = True
    for i in range(2,N):
        if N % i == 0:
            # 소인수 분해 가능 상태면 False로 변환
            stop = False
    # 더이상 분해가 되지 않으므로 
    if stop == True:
        print(N)
        break
#==================================================
    for i in range(2,N):
        # i는 N보다 작아야 약수가 될수 있다.
        if i < N:
            # N 을 i로 나눴을 때 나누어 떨어지면 i는 약수다.
           if N % i == 0:
                #i 출력
                print(i)
                # N 값 변경
                N = N//i
                # 처음부터 for문 시작
                break
# 다른 풀이
n = int(input())

if n == 1:
    print('')

# 2부터 하나씩 나눠보기
for i in range(2, n+1):
    if n % i == 0:
    	#해당 숫자로 나눌 수 없을 때까지 나누기
        while n % i == 0:
            print(i)
            n = n / i
# 해당 풀이는 첫번째 for문으로 가장 작은 소인수를 찾고 
# 그소인수로 최대한 나눈뒤
# 다음 소인수를 찾아 또 같은 방식으로 나눠서 더이상 분해 되지 않을때 까지 반복한다.
# 이 방식이 풀이는 아주 간단하다는 장점이 있지만 수행 시간에서 1400ms 가 걸려 나의 풀이(344ms)보다 4배 정도 시간이 더 걸린다는 단점이 있다. 