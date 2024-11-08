N = int(input())
list_a = input().split()
count = 0
for i in range(N-1):
    if list_a[i] != list_a[i+1]:
        count += 1
print(count)

