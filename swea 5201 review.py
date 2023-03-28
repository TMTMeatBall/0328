T = int(input())

for tc in range(1, T + 1):
    # 컨테이너 수 :N 트럭수: M
    N, M = map(int, input().split())
    # N 개의 화물 무게
    weight = list(map(int, input().split()))
    # M 개의 트럭 적재 용량
    truck = list(map(int, input().split()))

    for i in range(len(weight)):
        for j in range(len(weight)):
            if weight[i] > weight[j]:
                weight[i], weight[j] = weight[j], weight[i]

    for i in range(len(truck)):
        for j in range(len(truck)):
            if truck[i] > truck[j]:
                truck[i], truck[j] = truck[j], truck[i]

    # print(weight)
    # print(truck)

    i = 0
    j = 0
    cnt = 0
    while True:
        if len(weight) == i or len(truck) == j:
            break

        if weight[i] <= truck[j]:
            cnt += weight[i]
            # print(weight[i],truck[j])
            i += 1
            j += 1
        elif weight[i] > truck[j]:
            # if i < len(weight) and weight[i+1] < truck[j]:
            i += 1
            # else:
            #     j += 1
            #     i += 1

    print(f'#{tc} {cnt}')