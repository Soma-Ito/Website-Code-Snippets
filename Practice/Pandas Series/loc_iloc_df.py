
'''
下記サイトからCSVファイルをダウンロードし、Pythonファイルと同じフォルダーに入れてください
csv download link: https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/problem12.html
'''

import pandas as pd
df = pd.read_csv("titanic.csv")

# iloc: interのindexを用いて行の行の情報を取得する方法
# df.iloc[[行], [列]]で複数の行列の情報を取得
print(df.iloc[0])
print(df.iloc[[0, 1], [0, 1]])

# loc: 実際のindex名を用いて行の行の情報を取得する方法
# df.loc[[行], [列]]で複数の行列の情報を取得
# ただし、行のindex名は数字なので行に関してはilocと同じ形になる
print(df.loc[0])
print(df.loc[[0, 1], ["Name", "Sex"]])

print(type(df.iloc[0]))
