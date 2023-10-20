import pandas as pd
dataset = pd.read_csv('trainIPAdb_u.csv')
X = dataset.iloc[:,0]
y = dataset.iloc[:,-1]
tem = []
word = {}
odd_letter = [',' , '.' , '।' ]
for i in range(0,len(X)):
    tem.append([X[i].split(' ') , y[i].split(' ')])
def clean(s):
    ans = ''
    for i in range(0,len(s)):
        if s[i] in odd_letter:
            pass
        else:
            ans += s[i]
    return ans

for i in tem:
    ban = i[0]
    ipa = i[1]
    l = len(ban)
    for j in range(0,min(len(ban) , len(ipa))):
        word[clean(ban[j])] = clean(ipa[j])
tem = []
for i in word:
    tem.append([i,word[i]])
df = pd.DataFrame(tem)
df.to_csv('Word_IPA.csv')