
'''
下記サイトからCSVファイルをダウンロードし、Pythonファイルと同じフォルダーに入れてください
csv download link: https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/problem12.html
'''

import pandas as pd
df = pd.read_csv("titanic.csv")

print(df["Fare"])
# print(type(df.Fare))

print(df[["Name", "Sex"]])

print(type(df["Fare"]))
