
# dictionaryの構文: {key: value, key: value}
employee = {"name": "Samurai", "age": 25, "salary": 1000000}

print(employee["name"])  # "name"の値を表示

employee["phone"] = "123 - 456"  # keywordと値を追加
employee.pop("phone")  # "phone"の値を削除

# dictionaryのkeywordの表示
for key in employee:
    print(key)

# dictionaryの値の表示
for value in employee.values():
    print(value)

# dictionaryのkeywordと値の表示
for key, value in employee.items():
    print(key, value)
