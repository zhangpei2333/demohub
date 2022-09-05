"""
    这是多行注释
"""
""" #   这是单行注释

# 1.python数据的类型
print("hello world")    # 字符串
print(2333)         # 整数
print(2.333)        # 小数
print(True)         # 布尔值
print(False)        # 布尔值
print(())           # 元组
print([])           # 数组
print({})           # 字典

# 2.字符串的拼接
print("哈哈",2333,"呵呵")   
print("哈哈"+"呵呵")
print("23"+"33")
print(23+33)

# 3.python的数学运算
print("哈哈"*3)
print((9+1)*4)
print(2>3)


# 4.input——输入
# 变量
# 赋值
a = "张三"  # 把张三这个值赋值给了a这个变量
print(a)

b = input("请输入：")
print("input获取的内容",b)

c = input("请输入：")
d = input("请输入：")
print("拼接的结果：",c+d)


# 5.数据格式的转换
    # 1.任何数据类型都能转换为字符串
    # 2.空的字符类型无法转换
    # 3.整数和小数可以互相转换
    # 4.字符串转换为其他类型数据,需满足【长得像】的条件


f = type(2333)
print(f)

print(type("字符串")) # /str
print(type(2333))   # /int
print(type(2.333))  # /float
print(type(True))  #  /bool
print(type(()))   #  /tuple
print(type([]))   #  /list
print(type({}))  #  /dict 


c = int(input("请输入："))
d = int(input("请输入："))
print("计算的结果：",c+d)

# 6.len()  /获取字符串长度，支持字符串、元组、数组、字典
a = "adsklfjaksdfjaoifj"
print(len (a))



# 练习：通过代码获取两段内容，并计算他们的长度的和
# 方案一：
a = input("获取的内容1:")
b = input("获取的内容2:")
print("这是输入的内容的长度的和：",len((str(a+b))))

# 方案二：
c = len(str(input("获取的内容1:")))
d = len(str(input("获取的内容2:")))
print("这是输入的内容的长度的和：",c+d)

print("hello world!") """