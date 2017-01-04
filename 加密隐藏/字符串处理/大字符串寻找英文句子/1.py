<<<<<<< HEAD
# -*- coding:utf-8 -*-

'''
@用pypy去运行

#定义寻找字串位置的函数
#subString:子串
#fullString:完整字符串
#indexs:字串出现的所有位置
#即接受子串和完整字符串，返回子串在完整字符串里出现的所有位置
#例如findSubStr('hi','hiworldhiworld')得到[0,7]

'''

def findSubStr(subString,fullString):
    indexs = []
    fullLength = len(fullString)
    subLength = len(subString)
    for i in range(fullLength-subLength):
        if fullString[i:i+subLength] == subString:
            indexs.append(i)
    return indexs


#读取题目文件内的字符串
with open('whoiswoldy.txt','r') as f:
    s = f.read()


#逐行读取字典words.txt内的单词，寻找其在s内的所有位置
#places为单词出现过的所有位置
places = []
with open('English.txt','r') as f: 
    while 1:
        line = f.readline()
        line=line.strip('\n')
        if not line:
            break
        places += findSubStr(line,s)


#用pickle库将得到的位置数组places保存到result.txt中
import pickle
with open('result.txt','w') as f:
=======
# -*- coding:utf-8 -*-

'''
@用pypy去运行

#定义寻找字串位置的函数
#subString:子串
#fullString:完整字符串
#indexs:字串出现的所有位置
#即接受子串和完整字符串，返回子串在完整字符串里出现的所有位置
#例如findSubStr('hi','hiworldhiworld')得到[0,7]

'''

def findSubStr(subString,fullString):
    indexs = []
    fullLength = len(fullString)
    subLength = len(subString)
    for i in range(fullLength-subLength):
        if fullString[i:i+subLength] == subString:
            indexs.append(i)
    return indexs


#读取题目文件内的字符串
with open('whoiswoldy.txt','r') as f:
    s = f.read()


#逐行读取字典words.txt内的单词，寻找其在s内的所有位置
#places为单词出现过的所有位置
places = []
with open('English.txt','r') as f: 
    while 1:
        line = f.readline()
        line=line.strip('\n')
        if not line:
            break
        places += findSubStr(line,s)


#用pickle库将得到的位置数组places保存到result.txt中
import pickle
with open('result.txt','w') as f:
>>>>>>> 0b9dbfb320a073901bf33fe49fb8fcc85520109c
    pickle.dump(places,f)