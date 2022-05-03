t = open('危险化学品安全技术全书_部分3.txt')
print(t)

with open('危险化学品安全技术全书_部分0.txt','r',encoding='ansi') as f:
    for line in f.readlines():
        #line = line.strip("第一部分")
        line = line.split()
        #data.append(line)
        print(line)
