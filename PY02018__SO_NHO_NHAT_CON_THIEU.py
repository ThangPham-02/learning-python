N = int(input())
A = sorted(map(int, input().split()))
new = []
for number in range(min(A), max(A) + 1):
    if number not in A:
        new.append(number)
if len(new) == 0:
    print(max(A)+1)
else:
    print(min(new))