for _ in range(int(input())):
    announcement = input()
    if len(announcement) <= 100:
        print(announcement)
    if len(announcement) > 100 and not(announcement[100].isalpha()):
        print(announcement[0:100])
    if len(announcement) > 100 and announcement[100].isalpha():
        i = 100
        while announcement[i].isalpha():
            i -= 1
        print(announcement[0:i+1])