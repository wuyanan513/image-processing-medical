import pandas as pd
import numpy as np

# CSV
url = ("https://raw.github.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/tips.csv")
tips = pd.read_csv(url)

# 与 Excel 的文本导入向导一样，read_csv 可以采用多个参数来指定应如何解析数据。例如，如果数据改为制表符分隔，并且没有列名，pandas 命令将是
tips = pd.read_csv("tips.csv", sep="\t", header=None)
# 或者，read_table 是带有制表符分隔符的 read_csv 的别名
tips = pd.read_table("tips.csv", header=None)

# excel
tips_df = pd.read_excel("./tips.xlsx", index_col=0)
