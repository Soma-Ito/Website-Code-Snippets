
# printに関するdocumentationを表示
help(print)

# sep: 値を区切るためにの値(default: ' ')
# end: 最後の値を表示後の設定(default: '\n')
print(1, 2, 3, 4, 5, sep='|', end=' --- ')
print(1, 2, 3, 4, 5, sep=':')

# file: printの結果を表示させるfile(default: sys.stdout)
with open('help.txt', mode='w') as help_txt:
    print(1, 2, 3, 4, 5, sep='|', end=' --- ', file=help_txt)
    print(1, 2, 3, 4, 5, sep=':', file=help_txt)


import time

# 全てのnumが一斉表示
for num in range(4):
    time.sleep(1)
    print(num)

# numが順に表示
for num in range(4):
    time.sleep(1)
    print(num, flush=True)
