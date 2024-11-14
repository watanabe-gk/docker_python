import numpy as np

# ベクトルの定義
x = np.array([1, 2, 3])
y = np.array([2, 3.9, 6.1])

print("===== 平均の算出 =====")
print(f"xの平均: {x.mean():.2f}")
print(f"yの平均: {y.mean():.2f}")
print()

print("===== 中心化 =====")
xc = x - x.mean()
yc = y - y.mean()
print(f"x 中心化: {xc}")
print(f"y 中心化: {yc}")
print()

print("===== 要素積 =====")
xx = xc * xc
xy = xc * yc
print(f"x の要素積 (xc * xc): {xx}")
print(f"x, y の要素積 (xc * yc): {xy}")
print()

print("===== 傾きの計算 =====")
a = xy.sum() / xx.sum()
print(f"傾き a: {a:.2f}")
print()