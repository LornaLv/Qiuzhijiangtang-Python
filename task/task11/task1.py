# Date: 2023/3/8 上午11:08
def copyBigfile():
    old_file = input('请输入要备份的文件名')
    file_list = old_file.split('.')
    new_file = file_list[0] + '备份.' + file_list[1]
    try:
        with open(old_file, 'r') as old_f, open(new_file, 'w') as new_f:
            while True:
                content = old_f.read(1024)
                new_f.write(content)
                if len(content) < 1024:
                    break
        pass
    except Exception as e:
        pass

copyBigfile()