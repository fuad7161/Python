import sentecce_making as sm
import pandas as pd
dataset = pd.read_csv('trainIPAdb_u.csv')
X = dataset.iloc[:10,0]
y = dataset.iloc[:10,-1]
ans = []
for i in X:
    ans.append(sm.bangla_to_IPA(i))
for i in range(len(X)):
    print(X[i])
    print(ans[i])
    print(y[i])