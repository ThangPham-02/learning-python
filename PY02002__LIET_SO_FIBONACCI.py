fibonacci = [0,1]
for i in range(2,93):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
for _ in range(int(input())):
    a, b = map(int, input().split())
    for fibo_number in range(a, b+1):
        print(fibonacci[fibo_number], end = ' ')
    print('')