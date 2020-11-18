
text = 'I like dogs and cats'

# 空白を含め、n文字目 = stringのindex n-1
# ただし、indexは0からスタート
print(text[0], text[1], text[2])

# str.upper()はstringの文字全てを大文字に
print(text.upper())

# ただし、str.upper()は元々のデータを変換するものではない
print(text)

# 変数に割り当ては可能
upper_text = text.upper()
print(upper_text)

# stringの文字全てを大文字に
print(text.upper())

# stringの文字全てを小文字に
print(text.lower())

# stringの最初の文字を大文字に
print(text.capitalize())

# string内のsの数をカウント
print(text.count('s'))

# string内のdogの位置を確認
print(text.find('dogs'))
print(text.find('bird'))

# string内の'I like'を'He likes'に変換
print(text.replace('I like', 'He likes'))


# 大文字・小文字の区別が必要な例
if text.lower() == 'I like Dogs And Cats':
    print(True)
else:
    print(False)


if text.lower() == 'I Like Dogs And Cats'.lower():
    print(True)
else:
    print(False)
