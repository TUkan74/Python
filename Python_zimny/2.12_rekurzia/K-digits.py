K, N = list(map(int, input().split()))

def solve(word, s, d):
    if d == K:
        if s == N: print(word)
        return
    if word == "":
        rnge = list(range(1, min(10, N - s + 1)))
    else:
        rnge = list(range(0, min(10, N - s + 1)))

    for i in rnge:
        solve(word + str(i), s + i, d + 1)

solve("", 0, 0)

