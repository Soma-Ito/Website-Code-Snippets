
# listは[ ]で囲まれたもので、区切りに,(コンマ)を用います
# indexは0から始まります

lst = ["breakfast", 10, True]

lst.pop()  # 最後に追加されたデータを除去
lst.append(False)  # listの最後にFalseを追加
lst[0] = "lunch"  # 0番目のindexの値を"lunch"に置換

lst_lenth = len(lst)  # listのデータの総数

# listのitemを表示させる2種類の方法
for item in lst:
    print(item)

for index in range(lst_lenth):
    print(lst[index])
