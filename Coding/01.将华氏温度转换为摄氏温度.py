# -*-coding:utf-8-*-

#test01. 将华氏温度转换为摄氏温度公式为： C = (F - 32)div1.8
"""
将华氏温度转换为摄氏温度
Version:1.0
Author:Jun
"""
print('将华氏温度转换为摄氏温度')
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
# print('%.1f 华氏度 = %.1摄氏度' %(f,c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
