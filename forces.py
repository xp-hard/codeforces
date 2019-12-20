pices, meters = map(int, input().split())
l = sorted(list(map(int, input().split())))
zabor = [0 for i in range(pices)]

bag = [[0 for j in range(meters + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if l[i - 1] == j:
            bag[i][j] = 1
        if bag[i - 1][j] > 0:
            bag[i][j] = bag[i - 1][j]
            if j + l[i - 1] <= m:
                bag[i][j + l[i - 1]] = bag[i][j] + 1
"""for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(bag[i][j], end=' ')
    print()"""
way = []
cing = bag[-1][-1]
i, j =  n, m
while 1:
    #print(bag[i][j], i, j)
    if bag[i][j] == 0:
        break
    if i - 1 > 0 and bag[i - 1][j]:
        i -= 1
    else:
        for k in range(n):
            #print(l[k], end=' ')
            if j - l[k] >= 0 and bag[i][j - l[k]] == bag[i][j] - 1:
                way.append(l[k])
                j -= l[k]
print(*reversed(way))