
# forループの基本的な考え方
# 1. 基本形の作成
# 2. forループで変数を変化させる
# 3. 反復作業にindent(段差)をつける

# ループがない基本形(i=0の場合)の作成
i = 0
print(i)

# range(0, 5, 1) = 0から5まで1ずつ上がっていく整数
# ただし5は含まない
for i in range(0, 5, 1):
    print(i)

# range(0, 5, 1) = range(0, 5) = range(5)と省略できます
for j in range(0, 5):
    print(f"j is {j}")

for k in range(5):
    print(f"k is {k}")
