def runn(lst):  # 연속인 숫자가 3개 이상
    llst = sorted(lst)
    # 가져온 리스트에서 연속되는지 알아보는 방법?
    n = len(llst)
    for i in range(0, n - 2):
        if (llst[i] + 1) in llst and (llst[i] + 2) in llst:  # -2까지만 i세고 i+1,i+2 체크
            return True
    return False


def triplet(lst):  # 같은 숫자가 3장 이상

    n = len(lst)
    for i in range(n):
        if lst.count(lst[i]) >= 3:  # 받은 리스트에서 갯수 count
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    N = len(cards)
    A = []
    B = []
    for i in range(N // 2):
        A.append(cards[2 * i])
        B.append(cards[2 * i + 1])
        # 먼저?
    for i in range(4):
        # 4로 해야 6장을 채우는 때까지 체크가 가능함 3개씩만 받고 넘어가고 있음
        # 정렬시켜야 하는 이유? run 판단을 할 떄에 들어가는 인풋이 3,4,5,6으로 잘려서 들어가기 때문에 차례는 잡혀 있으므로 연속이 있는지 없는지만 파악하면 되므로 def run(lst)함수는 sort를 내장하고 있어야 한다.
        player_1 = runn(A[:i + 3]) or triplet(A[:i + 3])
        if player_1:
            result = 1
            break
        player_2 = runn(B[:i + 3]) or triplet(B[:i + 3])
        if player_2:
            result = 2
            break
        else:
            result = 0
    print(f'#{tc} {result}')
# 12장을 먹는데, 교대로 1장씩 나눈다. 6장을 채우기 전이라도 먼저 run(연속된 숫자가 3개이상)또는 triplet(같은 숫자가 3개 이상)
# 승자 표현은 무승부를 0으로 0,1,2 로 나타낸다
