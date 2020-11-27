"""
输入一个正整数判断它是否为素数
(素数:指的是只能被1和自身整除的大于1的整数)

Version: 0.1
Author: Jun
"""

print('判断一个正整数是否为质数')
num = int(input('请输入一个正整数:'))
end = int(num ** 0.5)
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是质数')
else:
    print(f'{num}不是质数')