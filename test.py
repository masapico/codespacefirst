import pandas as pd

df = pd.read_csv('aaa.csv', encoding='utf-8', sep='\t')

print(len(df))