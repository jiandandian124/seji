import jieba

"""data = []
f = open('危险化学品安全技术全书_部分1.txt',encoding='ansi')
line = f.read()
line = line.strip("第一部分")
line = line.split()
for i in line:
  data.append(i)

print(data)"""

data = []
with open('危险化学品安全技术全书_部分1.txt',encoding='ansi') as f:
    for line in f.readlines():
        #line = line.strip("第一部分")
        line = line.split('第一部分')
        #data.append(line)
        print(line)
