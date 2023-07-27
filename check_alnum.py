import pandas as pd

# 仮のデータフレームを作成します
data = {'Column1': ['abcd', '1234', 'abcd1234', 'abc@', '123@']}
df = pd.DataFrame(data)

# 'Column1' の各要素が英数字だけから構成されているかをチェックします
df['is_alnum'] = df['Column1'].apply(lambda x: x.isalnum())

print(df)

# Polars版
import polars as pl
import re

# 仮のデータフレームを作成します
data = {'Column1': ['abcd', '1234', 'abcd1234', 'abc@', '123@']}
df = pl.DataFrame(data)

# 正規表現を使って英数字のみかをチェックします
df = df.with_column(df['Column1'].apply(lambda x: bool(re.match('^[a-zA-Z0-9]*$', x)), return_dtype=pl.Boolean, name='is_alnum'))

print(df)
