import os

# 使用 os.path.expanduser 将包含 ~ 的路径转换为绝对路径
path = os.path.expanduser('~/.cache/clip')
print(path)