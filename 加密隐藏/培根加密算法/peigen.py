# -*- coding:utf-8 -*-

'''
@培根加密算法
'''

string="ABAAAABABBABAAAABABAAABAAAAAABAAAAAAAABAABBBAABBAB"
dicts={'aabbb': 'H', 'aabba': 'G', 'baaab': 'R', 'baaaa': 'Q', 'bbaab': 'Z', 'bbaaa': 'Y', 'abbab': 'N', 'abbaa': 'M', 'babaa': 'U', 'babab': 'V', 'abaaa': 'I', 'abaab': 'J', 'aabab': 'F', 'aabaa': 'E', 'aaaaa': 'A', 'aaaab': 'B', 'baabb': 'T', 'baaba': 'S', 'aaaba': 'C', 'aaabb': 'D', 'abbbb': 'P', 'abbba': 'O', 'ababa': 'K', 'ababb': 'L', 'babba': 'W', 'babbb': 'X'}
sums=len(string)

j=5   ##每5个为一组

for i in range(sums/j):
	result=string[j*i:j*(i+1)].lower()
	print dicts[result],
