import pdfplumber as pb

file_handle = open('out.txt', mode='w', encoding='utf-8')
# 读取PDF文档
pdf = pb.open("F:\\pycharm\\seji\\suju\\pdf\\mulu\\易制毒目录.pdf")
# 绝对路径也可以这么写，下同
#    path = 'F:\\pycharm\\seji\\suju\\pdf\\mulu\\易制毒目录.pdf'
# 获取页数
a = len(pdf.pages)
print("当前页：", a)
print("-----------------------------------------")

i = 0
for i in range(0, a):
    first_page = pdf.pages[i]
    print("本页：", first_page.page_number)
    print("-----------------------------------------")
    # 导出当前页文本
    text = first_page.extract_text()
    print(text)
    file_handle.write(text)

