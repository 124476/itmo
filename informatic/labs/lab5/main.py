import pandas as pd

df = pd.read_excel("table.xlsx")

df.insert(1, "TTTT", 100)

print(df)