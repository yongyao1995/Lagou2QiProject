#列表是一组有序的数据组合，列表中的数据可以被修改
#列表定义与基本操作做

varlist1 = [1,2,3,4,5]
varlist2 = ['a', 'b,', 'c', 'd']
#列表的拼接。把多个列表的元素拼成一个列表
#res = varlist1+varlist2+[11, 12, 13]
#res = varlist1*3

# 检测元素是否存在于列表当中
res = 'a' in varlist1

#列表的索引操作
"""
 0    1    2    3
'a', 'b', 'c', 'd',
-4   -3   -2   -5 
"""
# res = varlist2[2]

# 通过下标修改元素
#varlist2[2] ='cc'

#不能通过下标添加元素
#varlist2[4] = 'ff'  #IndexError: list assignment index out of range

#向列表中追加元素
# varlist2.append('ff')

# res = len(varlist2)

#列表元素删除，通过下标进行元素的删除
# del varlist2[2]
print(varlist2)
res = varlist2.pop()
print(varlist2)


