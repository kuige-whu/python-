from collections import Counter

a = [1, 4, 2, 3, 2, 3, 4, 2]

b = Counter(a)  # 求数组中每个数字出现了几次
print(b)

print(b[2])  # 计算每个元素出现了几次


Counter({2: 3, 4: 2, 3: 2, 1: 1})
3