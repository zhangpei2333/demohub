# 元组、数组、字典的操作

# 元组
# a1 = (1,2,3,4,"哈哈","嘻嘻",True,False)
# print(a1)

# 下标，从0开始编号
# a2 = (1,2,3,4,"哈哈","哈哈","哈哈","嘻嘻",True,False)
# print(a2[4])
# print(a2[-1])
# print(a2.index("哈哈"))   #只能操作一层元组
# print(a2.count("哈哈"))   #只能操作一层元组

# 二维元组  /[][]并列取值
# b2 = (a2,"哈哈",5,6,7)
# print(b2[0][3])

# 切片
# b3 = a2
# print(b3[0:4])
# print(b3[4:7])
# print(b3[8:])


# 数组   /区别在于元组一旦写好以后无法修改，数组写好以后可以修改
# from doctest import REPORTING_FLAGS


# a3 = [1,2,3,4,"哈哈","嘻嘻",True,False]
# a3.append("test01")
# a3.insert(0,"test02")
# b4 = a3.pop(0)  # 剪切
# print(a3)
# print(b4)
# a3.remove(1)
# print(a3)


""" 
Python的语法
所有的方法都是小括号结尾。比如print(),input(),index()
元组、数组、字典的取值，都是用中括号。比如 a[0] 
 """


# 字典
""" 
1、字典的值没有顺序
2、字典的结构必须是兼职对的结构  key:Value 
"""
""" a5 = {
    "name1":"张三",
    "name2":"李四"
}
print(a5)

# 取值
print(a5["name1"])
# 新增
a5["name3"] = "王五"
print(a5["name3"])
# 修改
a5["name1"] = "张二"
print(a5["name1"])
# 取值
b6 = a5.get("name1")
print(b6)
# 剪切
b7 = a5.pop("name1")
print(b7)
print(a5)
# 更新
a5.update(name1="张一")
print(a5) """



""" 练习:
获取用户输入的个人信息，并且存储到字典中。
个人信息包括: name,age,sex """

""" a = input("请输入姓名：")
b = input("请输入年龄：")
c = input("请输入性别：")
user = {"name":a,"age":b,"sex":c}
print(user) """

""" name = input("请输入姓名：")
age = input("请输入年龄：")
sex = input("请输入性别：")
userinfo = {}
userinfo.update(name=name,age=age,sex=sex)
print(userinfo) """