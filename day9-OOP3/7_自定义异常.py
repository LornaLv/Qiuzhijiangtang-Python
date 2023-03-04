# Date: 2023/3/4 下午5:59
class ToolongMyException(Exception):
    def __init__(self,len):
        self.len=len
    pass

    def __str__(self):
        return f'您输入的姓名的长度是{self.len},超过合法长度了'

def name_Test():
    name=input('请输入姓名：')
    try:
        if len(name)>6:
            raise ToolongMyException(len(name))
        else:
            print(name)
    except ToolongMyException as result:
        print(result)
    finally:
        print('程序执行结束了')
name_Test()