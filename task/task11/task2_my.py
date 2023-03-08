# Date: 2023/3/8 上午11:39
import os


def renameFile(file_path):
    listRs = os.listdir(file_path)  # 得到该路径下所有的文件夹

    for fileItem in listRs:
        full_path = os.path.join(file_path, fileItem)  # 获取完整的文件路径
        if os.path.isdir(full_path):  # 判断是否是文件夹
            renameFile(full_path)  # 如果是一个文件夹，再次递归
        else:
            path, item = os.path.split(full_path)
            if path[-1] != '/':  # 判断用户输入的文件夹的路径是否在最后加上/
                path = path + '/'  # 给没有加/的加上/
            else:
                path = path  # 已经加上的就不再加/
            os.rename(path + item, path + "2023-03-08_" + item)
    else:
        return


renameFile('/home/lvshaolin/桌面/Python/求知讲堂Python/task/task11/TestFile/')
