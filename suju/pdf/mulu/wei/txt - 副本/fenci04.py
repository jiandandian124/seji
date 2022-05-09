import re

input = open('危险化学品安全技术全书_部分1.txt',encoding='ansi')
lines = input.readlines()
n = 0
content = ''
# tempName=''
tempDesc = ''
# tempCount=0
section_re = re.compile("^第一部分")
split_flag = u'第一部分'
for line in lines:
    data = line
    line = line.encode('ansi').decode('ansi')
    match = re.match(section_re, line.split())
    if match:
        # print line.split(u'节')[0]
        n += 1
        if n == 1:
            tempDesc = line.split(split_flag)[0]
            # tempName=line.split(split_flag)[1]
        if n == 2:
            n = 0
            tempcontent = content
            # print ('tempDesc is %s,tempName is %s'%(tempDesc.strip(),tempName))
            print('chapter title: {}'.format(tempDesc.strip()))
            # print ('tempCount is %s'%(tempCount))
            print('chapter Content {}'.format(tempcontent))
            content = ''
            # tempCount=0
            line = data

    else:
        if not match:
            datas = line.strip()
            if len(datas) == 0:
                content += '<p></p>'
            else:
                content += '<p>' + line.replace('\n', '').replace("'", "''") + '</p>\n'
            # tempCount+=len(datas)
        line = input.readline()