<<<<<<< HEAD
# -*- coding:utf-8 -*_


#读取题目字符串
with open('whoiswoldy.txt','r') as f:
    s = f.read()
#加载前一步得到的位置数据
import pickle
with open('result.txt','r') as f:
    b = pickle.load(f)
#将位置数据b，一个list转化为集合set，即可实现去重复处理
#同时查找元素的时间由list的O(n)变为set的O(1)，因为set是hashable的
setb = set(b)

#den为密度统计，每个元素的形式为(int位置，int密度)
den = []
for number in setb:
    k = 1 
    for i in range(number,number+100):
        if i in setb:
            k += 1
    den.append((number,k))

#根据密度进行排序
sortedDen = sorted(den,key=lambda x:x[1],reverse=True)
#输出密度排名前10的位置
print sortedDen[0:10]
index = sortedDen[0][0]
=======
# -*- coding:utf-8 -*_


#读取题目字符串
with open('whoiswoldy.txt','r') as f:
    s = f.read()
#加载前一步得到的位置数据
import pickle
with open('result.txt','r') as f:
    b = pickle.load(f)
#将位置数据b，一个list转化为集合set，即可实现去重复处理
#同时查找元素的时间由list的O(n)变为set的O(1)，因为set是hashable的
setb = set(b)

#den为密度统计，每个元素的形式为(int位置，int密度)
den = []
for number in setb:
    k = 1 
    for i in range(number,number+100):
        if i in setb:
            k += 1
    den.append((number,k))

#根据密度进行排序
sortedDen = sorted(den,key=lambda x:x[1],reverse=True)
#输出密度排名前10的位置
print sortedDen[0:10]
index = sortedDen[0][0]
>>>>>>> 0b9dbfb320a073901bf33fe49fb8fcc85520109c
print s[index:index+150]