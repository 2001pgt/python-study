# 골드바흐 파티션 17103
# 문제
# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

# 출력
# 각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.

# 풀이
# 입력
import sys
input = sys.stdin.readline
T = int(input().strip())

# 소수 판별 함수
def Check_sosu(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for _ in range(T):
    # 짝수 n 입력
    n = int(input().strip())
    # 골드바흐 파티션 찾기
    # 두 소수의 합이 n 이 되면 됨 = 하나의 소소를 n에서 뺀 값이 소수가 되야한다.
    result = 0
    for i in range(1,n//2 + 1):
        if Check_sosu(i) == True and  Check_sosu(n-i) == True:
            if Check_sosu(n-i) == True:
                result += 1
    print(result)
    
# 이렇게 하면 당연히 시간 초과다 
# 속도를 개선하기위해 n 이 입력되면 바로 소수리스트를 만들어 버리고 여러번 소수 판단을 할필요를 없애겠다.
import sys
input = sys.stdin.readline

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= limit:
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
        p += 1
    return sieve

T = int(input().strip())

# 제한 범위를 설정합니다. 문제에 따라 변경할 수 있습니다.
limit = 1000000
sieve = sieve_of_eratosthenes(limit)

for _ in range(T):
    n = int(input().strip())
    result = 0
    for i in range(2, n // 2 + 1):
        if sieve[i] and sieve[n - i]:
            result += 1
    print(result)

