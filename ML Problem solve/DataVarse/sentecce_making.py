import okkhor as borno
import word_IPA_separation as direct_ipa
import Making_banjon_with_sorborno as Mbws
def get_ipa(s):
    ans = ''
    for i in s:
        if i in borno.get_ipaa:
            ans += borno.get_ipaa[i]
        else:
            ans += i
    #print(ans)
    return ans
def ipa(s):
    # prev = s
    # s = direct_ipa.clean(s)
    if s in direct_ipa.word:
        ans = direct_ipa.word[s]
        return ans
    

    #real coding start from here...
    # seperate okkhor like ডিশনাল -> ডি শ না ল
    okhor = []
    i = 0
    prev = ''
    while i< len(s):
        cur = s[i]
        if cur in borno.Sorborno_kar:
            cur = prev+cur
            okhor = okhor[:-1]
        if ord(s[i]) in borno.hosonto:
            if(i+1<len(s)):
                cur = prev+s[i+1]
            i += 1
            okhor = okhor[:-1]
        if cur in borno.Special_word_IPA:
            cur = prev+cur
            okhor = okhor[:-1]
        okhor.append(cur)
        prev = okhor[-1]
        i+=1
    #print(okhor)
    # return okhor
    ans = ''
    for i in okhor:
        ans += get_ipa(i)
    return ans

def bangla_to_IPA(s):
    ans = ''
    for i in s.split(' '):
        ans += ipa(i)
        ans += ' '
    return ans[:-1]

#'অ্যাডিশনাল'
#a = 'একাত্তর দ্বন্ধ হুররান স্ফটিক স্বচ্ছ হার্রাম হ্মখানর্ষ্ণ্য র্ষ্ণ্যর্হ্যর্শ্ব'
a = '১৯'
bn = bangla_to_IPA(a)
print(bn)