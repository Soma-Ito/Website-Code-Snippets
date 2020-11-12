
# whileループの基本的な考え方
# 1. 基本形の作成
# 2. whileループの条件を設定する
# 3. 反復作業にindent(段差)をつける
# 4. whileループ内で変数を変化させる

# Excercise 1 Answer
int_variable = 5

# Excercise 2 Answer
print(int_variable + int_variable)
print(int_variable - int_variable)
print(int_variable * int_variable)
print(int_variable / int_variable)

# Excercise 3 Answer
while int_variable >= 1:
    print(int_variable + int_variable)
    print(int_variable - int_variable)
    print(int_variable * int_variable)
    print(int_variable / int_variable)
    int_variable -= 1 # int_variable -= 1: int_variable = int_variable - 1
