
x = "10"
print(type(x))  # xのデータタイプを表示

int_x = int(x)  # xをintegerに変換
print(int_x, type(int_x))

float_x = float(x)  # xをfloatに変換
print(float_x, type(float_x))

str_x = str(int_x)  # int_xをstringに変換
print(str_x, type(str_x))

complex_x = 2j  # complexタイプのデータを割り当て(使用機会はほとんどありません)
print(complex_x, type(complex_x))

bool_yes = True  # Falseはyesと同義です
bool_no = False  # Falseはnoと同義です
print(type(bool_yes), type(bool_no))
