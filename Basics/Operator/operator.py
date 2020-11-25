
# --- operator --- #
# 演算記号
print(5 + 5)  # 5 + 5
print(5 - 5)  # 5 - 5
print(5 * 5)  # 5 × 5
print(5 / 5)  # 5 ÷ 5
print(5 // 2)  # 5 ÷ 2の整数部分
print(5 ** 2)  # 5²
print(5 % 2)  # 5 ÷ 2の余り

# 大小関係の記号
a, b = 10, 5
if a == b:
    print('a = b')
if a != b:
    print('a ≠ b')
if a > b:
    print('a > b')
if a >= b:
    print('a ≥ b')
if a < b:
    print('a < b')
if a <= b:
    print('a ≤ b')

# 基本的な数学的処理
print(abs(-5))  # 絶対値(absolute value)
print(round(3.141592, 4))  # 小数点第5位を四捨五入
print(sum([10, 20, 30, 40, 50]))  # listの値の合計

# 平均(2種類の方法)
import statistics
print(statistics.mean([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5]) / len([1, 2, 3, 4, 5]))
