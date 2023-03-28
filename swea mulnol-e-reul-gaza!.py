def solution(x,y,sum):








T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    #격자 밖으로 나가면 안됨
    #물인 칸으로 이동하기 위한 최소 횟수와 모든 이동횟수의 합을 출력하기.
    min_sum = 500

    solution()
    print(f'#{tc} {min_sum + }')

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue