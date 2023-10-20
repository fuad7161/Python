import word_IPA_separation as direct_ipa
soroborno = ['অ','আ','ই','ঈ','উ','ঊ','ঋ','ঌ','এ','ঐ','ও','ঔ']
banjonborno = ['ক','খ','গ','ঘ','ঙ','চ','ছ','জ','ঝ','ঞ','ট','ঠ','ড','ঢ','ণ','ত','থ','দ','ধ','ন','প','ফ','ব','ভ','ম','য','র','ল','শ','ষ','স','হ','ড়','ঢ়','য়']
Sorborno_kar = ['া','ি','ী','ু','ূ','ৃ','ৄ','ৢ','ৣ','ে','ৈ','ো','ৌ']
Soeborno_IPA = {'অ':'ɔ','আ':'ɐ','অ্যা':'æ','এ':'æ','ই':'i','ঈ':'i', 'উ':'u', 'ঊ':'u','এ':'e', 'ও':'o', 'অ':'o'}
Special_word_IPA = {'ঁ':'◌̃' , 'ঃ':'h', 'ঃ':'ɦ','ং':'ŋ'}
banjonborno_IPA = {'ক':'k','খ':'kʰ','গ':'ɡ','ঘ':'ɡʱ','ঙ':'ŋ','চ':'tʃ','ছ':'tʃʰ','জ':'z','ঝ':'dʒʱ',
                   'ঞ':'ɲ','ট':'ʈ','ঠ':'ʈʰ','ড': 'ɖ', 'ঢ':'ɖʱ','ঢ়':'ɽʱ','ণ': 'ɳ','ত':'t','থ':'tʰ',
                   'দ':'d','ধ':'dʱ', 'ন':'n','প':'pɔ','ফ':'ɸ','ব':'bɔ','ভ':'β','ম':'m', 
                   'য':'z','র':'r','ল':'l','ড়':'ɽ','শ':'ʃ','ষ':'ʃ','স':'ʃ',
                   'ৎ':'t','য়':'j','হ':'ɦ','ক্ষ':'kʰ',
                   'ও': 'w','উ':'w','য':'z','জ':'z'}



def get_ipa(s):
    if len(s) == 1:
        if s in soroborno:
            return Soeborno_IPA[s]
        if s in banjonborno:
            return banjonborno_IPA[s]
    elif len(s) == 2:
        if s[-1] in Sorborno_kar:
            # return banjonborno_with_soroborno[s]
            return ''
    return ''

def ipa(s):
    prev = s
    s = direct_ipa.clean(s)
    if s in direct_ipa.word:
        ans = direct_ipa.word[s]
        if prev[-1] in direct_ipa.odd_letter:
            ans += prev[-1]
        return ans
    ans = ''
    previous = ''
    for i in s:
        cur = i
        if i in Sorborno_kar:
            cur = previous+i
        ans += get_ipa(cur)
        cur = i

    return ans

def bangla_to_IPA(s):
    ans = ''
    for i in s.split(' '):
        ans += ipa(i)
        ans += ' '
    ans = ans[:-1]
    return ans
a = bangla_to_IPA('এরপরও তারা বকেয়া পরিশোধ করেনি।')
print(a)
# print(get_ipa('তা'))