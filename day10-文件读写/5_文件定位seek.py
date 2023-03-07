# Date: 2023/3/7 下午4:04

with open('test_备份.txt', 'rb') as f:
    data = f.read(21)
    print(data.decode('utf-8'))
    f.seek(-21, 1)  # 相当于光标又设置到了0的位置
    print(f.read(6).decode('utf-8'))
    f.seek(-9, 2)  # 2表示光标在末尾处
    print(f.read(5).decode('utf-8'))
