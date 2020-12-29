
import pandas as pd

df = pd.DataFrame()

df['x'] = [0, 1, 2]
df['y'] = [0, 2, 4]

df = df.append({'x': 3, 'y': 6}, ignore_index=True)


# 指定した行を削除
df.drop([3], inplace=True)
print(df)

# 指定した列を削除
df.drop(columns=['y'], inplace=True)
print(df)
