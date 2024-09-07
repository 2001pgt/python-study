# 별 찍기
#     *
#    ***
#   *****
#  *******
# *********
#N입력

N = int(input())

for i in range(N-1,-1,-1):
    print(' '*i,end='')
    for i2 in range(1):
        print('*'*((2*((N-1)-i))+1))