import okkhor as borno
import pandas as pd
banjonborno_with_soroborno = {}
for i in borno.banjonborno:
    for j in borno.Sorborno_kar:
        banjonborno_with_soroborno[i+j] = borno.banjonborno_IPA[i]+borno.soroborno_kar_IPA[j]


# df = pd.DataFrame(banjonborno_with_soroborno)
# df.to_csv('banjonborno_with_soroborno.csv')