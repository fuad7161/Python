import okkhor as borno
import pandas as pd
banjonborno_with_soroborno = []
for i in borno.banjonborno:
    for j in borno.Sorborno_kar:
        banjonborno_with_soroborno.append(i+j)
print(banjonborno_with_soroborno)

df = pd.DataFrame(banjonborno_with_soroborno)
df.to_csv('banjonborno_with_soroborno.csv')