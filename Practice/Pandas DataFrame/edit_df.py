
import pandas as pd

df = pd.DataFrame()


# 列を追加
df['x'] = [0, 1, 2]
df['y'] = [0, 2, 4]
print(df)

# 行を追加
df = df.append({'x': 3, 'y': 6}, ignore_index=True)
print(df)
