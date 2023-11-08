import okkhor as borno
import word_IPA_separation as direct_ipa
from utils import (float_int_extraction, fraction_to_words, generate_segments,input_sanitizer, whole_part_word_gen)

def number_to_bn_word(number):
    """
    Takes a number and outputs the word form in Bengali for that number.
    """

    generated_words = ""
    number = input_sanitizer(number)

    whole, fraction = float_int_extraction(number)

    whole_segments = generate_segments(whole)

    generated_words = whole_part_word_gen(whole_segments)

    if fraction:
        if generated_words:
            return generated_words + " দশমিক " + fraction_to_words(fraction)
        else:
            return "দশমিক " + fraction_to_words(fraction)
    else:
        return generated_words

def make_rules(s):
    tem = []
    prev = False
    for i in range(0,len(s)):
        if len(s[i]) == 1:
            pass
        elif len(s[i]) == 2:
            if s[i][0] in borno.banjonborno and s[i][1] in borno.banjonborno:
                tem.append(s[i][0])
                tem.append(s[i][1])
                tem.append('ও')
    tem.append(s[-1])
    # print(tem)
    return tem

def get_ipa(s):
    ans = ''
    if s in borno.get_ipaa:
        return borno.get_ipaa[s]
    
    for i in s:
        if i in borno.get_ipaa:
            cur = i
            if i == 'য়':
                cur = 'য়য়'
            elif i == 'য' and s[0] != i:
                cur = s[0]
            if cur in borno.get_ipaa:
                ans += borno.get_ipaa[cur]
        else: #special word..
            ans += i
    #print(ans)
    return ans
def ipa(s):
    # direct ipa
    # s = direct_ipa.clean(s)
    # if s in direct_ipa.word:
    #     ans = direct_ipa.word[s]
    #     return ans
    

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
                if s[i+1] in borno.get_ipaa:
                    cur = prev+s[i+1]
                else:
                    cur = prev
            i += 1
            okhor = okhor[:-1]
        if cur in borno.Special_word_IPA:
            cur = prev+cur
            okhor = okhor[:-1]
        okhor.append(cur)
        #rules 1
        if len(okhor):
            prev = okhor[-1]
        i+=1
    # print(okhor)
    # return okhor
    ans = ''
    okhor = make_rules(okhor)
    for i in okhor:
        ans += get_ipa(i)
    return ans

def bn_number(s):
    for i in s:
        if i in borno.number:
            pass
        else:
            return False
    i = 0
    while i<len(s) and s[i] == '০':
        i+=1
    if(i == len(s)):
        return False
    s = s[i:]
    return True
def bangla_to_IPA(s):
    # print(s)
    ans = ''
    for i in s.split(' '):
        if(bn_number(i)):
            ans += ipa(number_to_bn_word(i))
        else:
            ans += ipa(i)
        ans += ' '
    return ans[:-1]

#'অ্যাডিশনাল'
#a = 'একাত্তর দ্বন্ধ হুররান স্ফটিক স্বচ্ছ হার্রাম হ্মখানর্ষ্ণ্য র্ষ্ণ্যর্হ্যর্শ্ব শূন্য ঊনিশশ নভেম্বররর যায়না বকেয়া'
#a = '১৯ নভেম্বর নরেন্দ্র মোদি স্টেডিয়াম, বাংলাদেশ বিশ্বকাপ শিরোপা তুললো অন্যায়-অত্যাচার সম্পর্কে' 
# a = 'র্র‌্যানসমওয়্যার'
# bn = bangla_to_IPA(a)
# print(bn)