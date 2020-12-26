
dictionary = {'name': 'Samurai', 'age': 25, 'salary': 1000000}
print(dictionary)


# 複数のkeywordに1つのvalueを結びつける
# 元のdictionaryにkeywordがない場合は新たに追加
keys = ('name', 'job')
fromkeys_dict = dictionary.fromkeys(keys, 'Ninja')
print(fromkeys_dict)

copyed_dict = dictionary.copy()  # dictionaryをコピーして新たな変数に割り当て
lst = dictionary.values()  # dictionaryの全てのvalueをlistに変換


dictionary.get('name')  # 'name'の値を表示(keywordがない場合はNone)
dictionary.items()  # それぞれのitem(keyword+value)をtupleに入れたlistを作成
dictionary.keys()  # keywordのlistを作成
dictionary.setdefault('phone', '123-456')  # 'phone'のvalueを'123-456'に変更(keywordがない場合は新たに追加)
dictionary.update({'age': 30})  # 'age'のvalueを30に変更(keywordがない場合はNone)


dictionary.pop('age')  # keyword('age')とそのvalueを削除(keywordがない場合はerror)
dictionary.popitem()  # 最後に追加されたitemを削除
dictionary.clear()  # 全てのitemを削除
