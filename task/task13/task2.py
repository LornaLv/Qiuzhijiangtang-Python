# Date: 2023/3/15 上午10:12
# 验证用户名，长度为6-18位的英文字母组成
import re

res = re.match('[a-zA-Z]{6,18}', 'sdsddxppppppppppppacdb')
if res:
    print(res.group())
else:
    print('用户名错误')
