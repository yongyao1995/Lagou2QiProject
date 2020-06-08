
try:
    num1 = int(input("输入一个除数："))
    num2 =int(input("输入一个被除数："))
    print(num1/num2)
# except ZeroDivisionError:
#     print("被除数不能为空")
# except ValueError:
#     print("需要输入的数值型整数")
except:
    print("这是一个能用型异常")
else:
    print("程序没有发生异常")
finally:
    print('无论发没发生异常，都执行')

