P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    in_put = input().split()
    N, K = int(in_put[0]), int(in_put[1])
    S = ""
    for i in range(1, N+1):
        S = S + P[i-1] + S
    print(S[K - 1])


