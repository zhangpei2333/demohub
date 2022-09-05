# ----判断和循环----

# 1、判断

# a = 1
# b = 2

# if a == 1:
#     print("a=1")

# if b > a:
#     print("a比b大")
# else:
#     print("b比a大")

# age = int(input("请输入你的年龄："))
# if age > 60:
#     print("可以退休了")
# elif age > 30:
#     print("请保重身体")
# elif age > 20:
#     print("好好工作")
# else:
#     print("请好好读书")

# age = int(input("请输入你的年龄："))
# if age > 20 and age <= 30:
#     print("打工人")
# elif age >30 and age <= 60:
#     print("社畜")
# elif age > 60:
#     print("退休了")
# else:
#     print("好好读书！")

# == 等于
# != 不等于
# > 大于
# < 小于
# in 属于（被包含）
# is 等于（对象）
# not in 不属于（不被包含）
# not is 不等于（对象）

# a = "你好"
# b = ("你好","您好","她好")
# if a in b:
#     print("ok")
# else:
#     print("not ok")

# a = input("请输入：")
# if a in "0123456789":
#     a = int(a)
# else:
#     print("请输入正确的数字！")
#     exit()
# if a > 3:
#     print("大")
# else:
#     print("小")


# 循环
# 1、while循环
# a = 11
# while a < 10:
#     print("哈哈")
#     a = a + 1

""" 
练习
学生的成绩需要录入到系统中
N个学生需对应N个成绩
大于等于60分和小于60分需要分开存放
input
字典
数组
"""
# hlist = {}  #定义了一个空字典
# llist = {}  #定义了一个空字典
# slist = ["张三","张四","张五","张六","张七","张八"]  #定义了一个数组

# a = 0  #定了一个变量，用来控制数组下标的变化
# while a < len(slist):
#     chengji = int(input("请输入"+slist[a]+"的成绩："))
#     if chengji >= 60:
#         hlist[slist[a]] = chengji #通过新增的方式，把key和valu存在字典中
#     else:
#         llist[slist[a]] = chengji
#     a = a + 1  #控制下标变化，每次循环+1

# print("及格的同学",hlist)
# print("不及格的同学",llist)

# for循环 / 遍历

# a = (1,2,3,4,5,6,7,8,9)
# for i in a:
#     print(i)

# b  = list(range(100))  #自动生产了一个数列
# print(b)

# for i in range(0,10,2):
#     print(i)

""" 
练习
学生的成绩需要录入到系统中
N个学生需对应N个成绩
大于等于60分和小于60分需要分开存放
input
字典
数组
"""
# hlist = {}  #定义了一个空字典
# llist = {}  #定义了一个空字典
# slist = ["张三","张四","张五","张六","张七","张八"]  #定义了一个数组

# for i in slist:
#     chengji = int(input("请输入"+i+"的成绩："))
#     if chengji >= 60:
#         hlist[i] = chengji #通过新增的方式，把key和valu存在字典中
#     else:
#         llist[i] = chengji

# print("及格的同学",hlist)
# print("不及格的同学",llist)


""" 
练习
打印一个九九乘法表
"""

# for i in range(1,10):
#     for j in range(1,i+1):
#         # print(i,j)
#         print(i,"*",j,"=",i*j,end="  ")
#     print( )

""" 
练习1
通过print打印,实现红绿灯功能,红灯30秒,绿灯35秒,黄灯3秒
联系2
使用代码,实现一个注册的功能。用户输入密码和账号,要求账号为5-8位,密码6-12位,
并且账号必须为小写开头，储存在字典中。 
"""
# 练习1

# light = {"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in light:
#         for j in range(light[i]):
#             print(i,"倒计时:",j,"秒")

# 练习2
username = input("请输入账号:")
password = input("请输入密码:")
if len(username) >= 5 and len(username) <= 8 and [type(username) in ["int","str"]]:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
            if len(password) >= 6 and len(password) <= 12:
                print("注册成功!",{"账号":username,"密码":password})
            else:
                print("请输入符合规范的6-12位密码!")               
        else:
            print("账号必须为小写开头")          
else:
    print("请输入符合规范的5-8位账号!")
