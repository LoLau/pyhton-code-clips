from functools import reduce

__author__ = 'lg'

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 计算平方
# map 函数接收两个参数，第一参数是函数名func，第二个参数是可迭代对象，
# 对迭代对象中的每个元素执行func操作并返回可迭代对象
def map_test():
    def add(x):
        return x * x

    return map(add, arr)

print(list(map_test()))
# 结果 ：[1, 4, 9, 16, 25, 36, 49, 64, 81]


# 数组求和
# reduce函数接收两个参数，第一个是函数名func，第二个是可迭代对象，
# 把函数的结果继续和迭代对象中的下一个元素做累计计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def reduce_test():
    def add(x, y):
        return x + y

    return reduce(add, arr)

print(reduce_test())
# 结果：45
