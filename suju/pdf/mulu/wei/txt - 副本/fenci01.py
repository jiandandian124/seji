import re

target_dir = r'F:\pycharm\seji\suju\pdf\mulu\wei\txt - 副本\bu\\'
"""n = [1,2,3,4,5,6,7,8,9]
for i in n:
    l_array = []
    f=open('危险化学品安全技术全书_部分'+ str(i) + '.txt', encoding= 'ansi')
    line = f.read()
    l_a = line.split('第一部分')
    for l in l_a:
       l_array.append(l)
    for li in l_array:
        t = l_array.index(li)
        with open(target_dir + str(t) + ".txt",'w+',encoding='utf-8') as f_target:
            f_target.write(li)"""

def larray(n):
    i = n
    f = open('危险化学品安全技术全书_部分' + str(i) + '.txt', encoding='ansi')
    line = f.read()
    l_a = line.split('第一部分')
    return l_a

l_a1 = larray(1)
l_a2 = larray(2)
l_a3 = larray(3)
l_a4 = larray(4)
l_a5 = larray(5)
l_a6 = larray(6)
l_a7 = larray(7)
l_a8 = larray(8)
l_a9 = larray(9)
l_a = l_a1 + l_a2 + l_a3 + l_a4 + l_a5 + l_a6 + l_a7 + l_a8 + l_a9

print(len(l_a))


for li in l_a:
    t = l_a.index(li)
    with open(target_dir + str(t) + ".txt", 'w+', encoding='utf-8') as f_target:
        f_target.write(li)
