"""
用户身份验证

Version: 0.1
Author: Jun
"""
username = input("请输入用户名:")
password = input("请输入口令:")
# 用户名是admin且密码是123456则身份验证成功,否则验证失败
if username == 'admin' and password == '123456':
    print("身份验证成功!")
else:
    print("身份验证失败!")

"""
分段函数求值

Version: 0.1
Author: Jun
"""
"""
f(x) ={ 3x-5  (x>1)
        x+2 (-1<x<1)
        5x+3   (x<-1)
"""
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'f({x}) = {y}')