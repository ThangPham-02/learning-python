wishes = []
for _ in range(int(input())):
    wishes.append(input())
count_wishes = []
for sentence in wishes:
    if sentence not in count_wishes:
        count_wishes.append(sentence)
print(len(count_wishes))