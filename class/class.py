class Persion():  # 创建类
    name = "张永耀"  # 创建类的属性

    def get_name(self):  # 创建类的方法
        return "hello word"


print(Persion.name)
p = Persion()  # 类的实例化
print(p.name)  # 打印出类的属性
print(p.get_name())  # 打印出类的方法

# p.name = '张三'  # 属性重新赋值
Persion.name = "小张"
p.name = "黄花菜"
print(p.name)

p1 = Persion()
print(p1.name)
