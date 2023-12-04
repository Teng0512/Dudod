"""
-*- coding utf-8 -*-
@Time    :2023/12/3 19:36
@Author  :mila
@File    :my_error.py
@Software:PyCharm Community Edition
"""
# print("aa")

# assert 1==2

# print("bei".bei)
# import bei
# from sys import bei
# l=[]
# print(l[11])
# d={'name':'ll'}
# print(d['id'])


def add(a, b):
    print("ad开始执行")
    if not isinstance(a, int):
        raise ValueError(f"{a=},不是整数无法计算")

    if not isinstance(b, int):
        raise ValueError(f"{b=},不是整数无法计算")

    c = a + b
    print("ad结束执行")
    return c

sasdsdassdds

def mains():
    print("mains开始执行")
    print(add(1, "x"))
    print("mains结束执行")


if __name__ == "__main__":
    try:  # 开始捕捉异常
        mains()  # 可能会引发异常的代码
    except:  # 捕捉异常
        print("except")  # 出现异常时自动执行
    else:
        print("else")  # 没有出现异常时自动执行
    finally:
        print("finally")  # 不论是否出现异常，都会自动执行
