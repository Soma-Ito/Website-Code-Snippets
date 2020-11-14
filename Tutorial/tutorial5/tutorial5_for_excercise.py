
# forループの基本的な考え方
# 1. 基本形の作成
# 2. forループで変数を変化させる
# 3. 反復作業にindent(段差)をつける

# Excercise 1 Answer
int_variable = 5

# Excercise 2 Answer
print(int_variable + int_variable)
print(int_variable - int_variable)
print(int_variable * int_variable)
print(int_variable / int_variable)

# Excercise 3 Answer
for int_variable in range(5, 0, -1):
    print(int_variable + int_variable)
    print(int_variable - int_variable)
    print(int_variable * int_variable)
    print(int_variable / int_variable)
