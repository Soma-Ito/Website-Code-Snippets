
'''
下記サイトからCSVファイルをダウンロードし、Pythonファイルと同じフォルダーに入れてください
csv download link: https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/problem12.html
'''

import pandas as pd
df = pd.read_csv("titanic.csv", index_col='Name')
print(df.index)

df.sort_index(ascending=True, inplace=True)
print(df)

print(df.loc["Capt. Edward Gifford Crosby", "Age"])
print(df.iloc[0, 3])

