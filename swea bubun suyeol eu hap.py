def frac(i, j):
    if i == j:
        sum = 0
        cnt = 0
        for i in range(N):
            if bin[i] == 1:
                sum += A[i]
        if sum == K:
            for i in range(N):
                cnt += 1

            return print(cnt)
    else:
        bin[i] = 0
        frac(i + 1, j)
        bin[i] = 1
        frac(i + 1, j)


# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     A = list(map(int, input().split()))
#     bin = [0] * N
#
A = [1,2,1,2]
N = len(A)
K = 3
bin = [0] * N
frac(0, K)

# N = a리스트 요소의 갯수, k는 a의 부분 수열의 합이 k가 되는 경우의 수를 정답에 출력함
