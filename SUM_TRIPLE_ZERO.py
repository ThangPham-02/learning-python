for _ in range(int(input())):
    N = int(input())
    A = list(sorted(map(int, input().split())))
    count = 0
    for i in range(N): # N = len(A)
        left = i + 1
        right = N - 1
        while left < right:
            SUM = A[i] + A[left] + A[right]
            if SUM == 0:
                count += 1
                left += 1
            elif SUM > 0:
                right -= 1
            else:
                left += 1
    print(count)
