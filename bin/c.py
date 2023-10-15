soroborno = ['অ','আ','ই','ঈ','উ','ঊ','ঋ','ঌ','এ','ঐ','ও','ঔ']
banjonborno = ['ক','খ','গ','ঘ','ঙ','চ','ছ','জ','ঝ','ঞ','ট','ঠ','ড','ঢ','ণ','ত','থ','দ','ধ','ন','প','ফ','ব','ভ','ম','য','র','ল','শ','ষ','স','হ','ড়','ঢ়','য়']
Sorborno_kar = ['া','ি','ী','ু','ূ','ৃ','ৄ','ৢ','ৣ','ে','ৈ','ো','ৌ']
Soeborno_IPA = {'অ':'ɔ','আ':'ɐ','অ্যা':'æ','এ':'æ','ই':'i','ঈ':'i', 'উ':'u', 'ঊ':'u','এ':'e', 'ও':'o', 'অ':'o'}
Special_word_IPA = {'ঁ':'◌̃' , 'ঃ':'h', 'ঃ':'ɦ','ং':'ŋ'}
banjonborno_IPA = {'ঢ়':'ɽʱ','ঞ':'ɲ','ব': 'b', 'ভ': 'β', 'দ': 'd', 'ধ': 'dʱ', 'ড': 'ɖ', 'ঢ': 'ɖʱ', 'জ': 'z','য':'z','ঝ': 'dʒʱ', 'গ': 'ɡ', 'ঘ': 'ɡʱ', 'হ': 'ɦ', 'ক': 'k', 'খ': 'kʰ','ক্ষ':'kʰ', 'ল': 'l','ম': 'm', 'ন': 'n','ণ':'n', 'ঙ': 'ŋ', 'প': 'p', 'ফ': 'ɸ', 'র': 'r', 'ড়': 'ɽ','স': 's', 'শ': 'ʃ', 'ষ': 'ʃ', 'স': 'ʃ', 'ত': 't','ৎ':'t', 'থ': 'tʰ', 'ট':  'ʈ', 'ঠ': 'ʈʰ', 'চ': 'tʃ', 'ছ': 'tʃʰ', 'য়': 'j', 'ও': 'w','উ':'w', 'ণ': 'ɳ','য':'z','জ':'z'}

word = 'বলম'
ans = ''
for i in word:
    ans += banjonborno_IPA[i]
print(ans)