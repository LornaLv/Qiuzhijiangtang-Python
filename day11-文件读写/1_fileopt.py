# Date: 2023/3/6 下午9:26
# 文件的操作,默认的编码是GBK，这个是中文编码，最好的习惯是在打开一个文件的时候制定一个编码
# 1、打开文件open
fobj = open('./test.txt', 'w', encoding='utf-8')
# 2、读/写文件
fobj.write('人生苦短，我学Python\n')
fobj.write('狂风卷集着乌云')
# 3、保存文件
# 4、关闭文件
fobj.close()

# 以二进制的形式去写数据
#a 用于追加数据
file1 = open('./test1.txt', 'a')  # str--->byte
file1.write('在乌云和大海之间\n')
file1.close()


