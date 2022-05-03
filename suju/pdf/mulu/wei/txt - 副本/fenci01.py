import jieba


f=open('危险化学品安全技术全书_部分0.txt', encoding= 'utf-8')
line = f.read()
text = jieba.lcut(line)
f.close()
"""t = type(text)
print(t)"""
f1 = open('危险0.csv','w', encoding='utf-8')
for j in text:
    f1.write(j+'\n')
f1.close()