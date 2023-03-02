# Date: 2023/2/27 下午5:48
'''
小王身高1.75,体重80.5kg。请根据BMI公式（身高除以体重的平方）帮小王计算他的BMI指数，并根据BMI指数
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果
'''

height = float(input('请输入你的身高（米为单位）：'))
weight = float(input('请输入你的体重（千克为单位）：'))
bmi = weight / height / height
print(f'您的BMI值为：{bmi}')
if bmi <= 18.5:
    print('过轻')
elif 18.5 < bmi <= 25:
    print('正常')
elif 25 < bmi <= 28:
    print('过重')
elif 28 < bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')
