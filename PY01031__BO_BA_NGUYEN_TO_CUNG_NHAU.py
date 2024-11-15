import math

left, right = input().split()
left, right = int(left), int(right)
for a in range(left, right + 1):
    for b in range(a + 1, right + 1):
        if math.gcd(a,b) == 1:
            for c in range(b + 1, right + 1):
                if math.gcd(a, c) == 1 and math.gcd(b, c) == 1:
                    print(f"({a}, {b}, {c})")