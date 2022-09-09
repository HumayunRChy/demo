import pandas as pd
import itertools

df = pd.read_excel("data.xlsx", header=None, index_col=False, dtype=str)
df.columns = ['A']

comb = list(itertools.product(df['A'], repeat=4))
a = comb

for x in range(len(a)):
    print(a[x], file=open('comb.txt', 'a'))
