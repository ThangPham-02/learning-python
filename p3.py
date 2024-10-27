a = int(input())

def round_int(a, count):
    divisor = 10**count
    rounded_number = a
    if a %  divisor >= ( 5 * 10**(count-1) ):
        rounded_number = (a // divisor) * divisor + divisor
    if a %  divisor < ( 5 * 10**(count-1) ):
        rounded_number =  (a // divisor) * divisor
    return rounded_number

def rounder(a, count = 0):
    if a <= 10:
        return a
    count += 1
    print (count)
    if count == len(str(a)):
        return a
    print(round_int(a, count))
    return rounder(round_int(a, count), count)

rounder(a)




