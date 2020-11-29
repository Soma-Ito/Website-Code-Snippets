
lst = ["breakfast", "lunch", "dinner"]

# list内の値に関する操作
print("lunch" in lst)  # lst内に"lunch"の有無を確認
print(lst.index("lunch"))  # "lunch"のindexを取得
print(lst.count("lunch"))  # "lunch"の数を表示
print(lst[-1])  # 最後のindexの値を表示
print(lst[0:1])  # 特定のindex範囲を表示(index start:index end)

# listに新たな値を挿入
lst.insert(2, "lunch snack")  # 2番目のindexに"lunch snack"を挿入
print(lst)

# listに別のlistの値を挿入
lst2 = ["night snack", "tea"]
lst.extend(lst2)  # lst2の値をlstに追加
print(lst)

# listの値の削除
num_lst = [i for i in range(1, 11)]
num_lst.pop(0)  # 0番目のindexを削除
num_lst.remove(5)  # 5の値を削除
num_lst.clear()  # 全ての値を削除
print(num_lst)

# listの並び替え
lst = ["breakfast", "lunch", "dinner"]
lst.reverse()  # 逆のindex順に表示(-1 -> 1)
print(lst)
lst.sort()  # lstをアルファベット順に並び替え
print(lst)

num_lst = [i for i in range(1, 11)]
num_lst.sort()  # 小さい順に並び替え
print(num_lst)
num_lst.sort(reverse=True)  # 大きい順に並び替え
print(num_lst)
sorted_num_lst = sorted(num_lst)  # 小さい順に並び替え(別の方法)
print(sorted_num_lst)

# listの最大値・最小値
print(max(sorted_num_lst))  # listの最大値
print(min(sorted_num_lst))  # listの最小値

# listとstringの変換
comma_lst = ', '.join(lst)  # lstの値を', 'で区切り、1つのstringに合成
print(comma_lst)
meal_lst = comma_lst.split(', ')  # stirngの値を', 'で区切り、listを作成
print(meal_lst)
