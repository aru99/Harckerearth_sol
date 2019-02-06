from collections import Counter

cnt = Counter()
for num in [1, 2, 3, 4, 1, 2, 3, 1, 2, 3]:
    cnt[num] += 1

print(cnt)
