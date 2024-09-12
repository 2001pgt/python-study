# 문제
# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# 출력
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

# 둘째 줄에는 중앙값을 출력한다.

# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

# 넷째 줄에는 범위를 출력한다.

# 풀이
import sys
input = sys.stdin.readline
# 입력
n = int(input().rstrip())
nums = []   
for i in range(n):
    x = int(input().rstrip())
    nums.append(x)
# 산술평균 소수점 첫째자리에서 반올림
res1 = sum(nums) / n
res1 = round(res1)
print(res1)
# 중앙값
sorted_nums= sorted(nums)
print(sorted_nums[len(sorted_nums)//2])
# 최빈값
# 최빈값을 구하는 함수
def choi_bin_gap(A):
    # 입력받은 수의 개수가 1면 첫번째 인덱스 숫자 리턴
    if len(A) < 2:
        return A[0]
    # 숫자를 담을 리스트
    num_bucket =[]
    # 빈도수를 담을 리스트
    size_bucket = []
    # 빈도수
    cnt = 1
    for i in range(len(A)):
        # 첫 인덱스의 숫자는 num_bucket에 저장
        if i == 0:
            num_bucket.append(A[0])
        # 그 외는
        else:
            # 전 숫자와 현재 숫자가 같다면
            if A[i] == A[i - 1]:
                # 빈도수 +1
                cnt += 1
                # 마지막 숫자면
                if i == len(A)-1:
                    # 사이즈 버킷에 현재 빈도수 추가
                    size_bucket.append(cnt)
            # 같지 않다면
            else:
                # size_bucket에 빈도수cnt추가후 
                size_bucket.append(cnt)
                # 빈도수 1 로 초기화
                cnt = 1
                # num_bucket에는 현재 숫자 추가
                num_bucket.append(A[i])
    # 루프가 끝난후 빈도수 리스트에서 가장 큰 수 추출
    max_size = max(size_bucket)
    
    # 가장 큰수의 인덱스를 리스트로 나열(1개든 여러개든 상관없음)
    max_indices = [i for i, value in enumerate(size_bucket) if value == max_size]
    
    # 빈도수 리스트에서 가장 큰 수의 인덱스 = 전체 숫자중 최빈값의 인덱스 

    # 만약 여러개면
    if len(max_indices) > 1:
        # 2번 째 값이 최빈값중 두번째로작은 인덱스 이므로 
        # 해당 값을 num_bucket의 인덱스값으로 하여 리턴
        return num_bucket[max_indices[1]]
    else:
        # 한개면 해당 수로 인덱스 하여 출력
        return num_bucket[max_indices[0]]
# 최빈값 출력
print(choi_bin_gap(sorted_nums))

# 범위
print(sorted_nums[-1] - sorted_nums[0])


