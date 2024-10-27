'''
def gcd(a, b):
    sub = b - a
    if a == b:
        return a
    if sub < a :
        if  a % sub == 0:
            return sub
        else:
            return gcd(sub, a)
    if sub > a :
        if sub % a == 0:
            return a
        return gcd(a, sub)


print(gcd(16,22))

--------------

a = int(input())
b = int(input())

def gcd(a,b):
    ucln = b % a
    if ucln == 0:
        return a
    if a == b:
        return a
    if a % ucln == 0:
        return ucln
    else:
        return gcd(ucln,a)
print(gcd(a,b)) 
'''



