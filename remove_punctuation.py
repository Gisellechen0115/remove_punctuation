#punctuation ="!@#$%^&*()_+=~`|\}]{{"':;?/>.<,"
poem ='''When I was young. I loved to swim.
'''
import string

def remove_punctuation(s):
    s_sans_punct =""
    for letter in s:
        if letter not in string.punctuation:
            s_sans_punct += letter
    #return s_sans_punct
    wds = s_sans_punct.split()
    return wds



def count_letter_in_world(letter, wds):
    count = 0
    for ch in wds:
        for w in ch:
            if w == letter:
                count += 1
    #return count
    print("Your text contains ", count, " of which", len(wds), "contain an", letter)


print(remove_punctuation(poem))
count_letter_in_world("e", remove_punctuation(poem))


def myreplace(old, new, s):

    result = new.join(s.split(old))
    return result

print(myreplace(" ", "**", "worlds will now be separated by stars."))

def cleanworld(w):
    sig ="!@#$%^&*()_+}{[]"":?><,"
    newword = ""
    for letter in w:
        if letter not in sig:
            newword += letter
    return newword

print(cleanworld("I love $money, this is good!"))


def clean2(w):
    sig ="!@#$%^&*()_+}{[]"":?><,"
    w1 = w.strip(sig)  #strip只能清除兩兩端
    return w1

print(clean2("@I love $money, this is good!"))



# python内建的split()函数只能使用单个分隔符   
            
#https://www.cnblogs.com/volcao/p/8780972.html
import string

def clean3(s):
    for c in string.punctuation:
        s = s.replace(c,"") #要給同樣的名子
    return s

print(clean3("@I love $money, this is good!"))

def clean5(s):
    exclude = set(string.punctuation)
    out = ''.join(ch for ch in s if ch not in exclude)
    return out
      
print(clean5("@I love $money, this is good!"))

"""
def clean4(w):
    #patten = r'([!. @ . #. $. %. ^. &. *. (. ). _. +. }. {. [. ]. :. ?. >. <. ,. \ })
    patten = r'(!@#$%^&*()_+}{[]"":?><,])
    newword = re.split("!@#$%^&*()_+}{[]"":?><,)*", w)
    return newword

print(clean4("@I love $money, this is good!<,"))    
        
    #. :匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用像 '[.\n]' 的模式 
    #https://www.runoob.com/python/python-reg-expressions.html#flags
    
"""
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'

print(re.split(r'[;,\s]\s*', line))
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

#https://blog.csdn.net/weixin_42268081/article/details/106720822?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-4.no_search_link&spm=1001.2101.3001.4242

import re, timeit

s = "@I love $money, this is good!<,"
def clean5(s):
    s = re.S(r'[^\w\s]','',s)  #re.sub(replace, string, count=0) 替換字符串
       #[^...] 不包含   \w 匹配字母、數字 \s 	匹配任意空白字符
    return s

print(clean5("@I love $money, this is good!<,")) 
print("clean5 :",timeit.Timer('f(s)', 'from __main__ import s,clean5 as f').timeit(1000000))

