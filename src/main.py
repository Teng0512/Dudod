"""
-*- coding utf-8 -*-
@Time    :2023/12/3 18:34
@Author  :mila
@File    :main.py
@Software:PyCharm Community Edition
"""
"""
需求：编写一个程序，可以用来列出文件夹中的全部文件
前提：指定文件夹
步骤：
1.查询文件夹中的内容
2.如果查询结果也是文件夹的话，重复第一步
3.如果查询结果是文件，打印文件的名称或路径
"""
import logging
import os

path = "./"


def get_file_with_path(path):
    f_list = os.listdir(path)
    logging.warning(f"{f_list=}")
    only_file_list = []
    for f in f_list:
        full_path = os.path.join(path, f)  # 完整路径
        if os.path.isfile(full_path):
            only_file_list.append(full_path)
        # 如果是一个目录
        elif os.path.isdir(full_path):
            only_file_list.extend(get_file_with_path(full_path))
        else:
            logging.warning(f"{full_path=}不是文件也不是目录")
    logging.warning(f"{only_file_list=}")
    return only_file_list


print(get_file_with_path(path))
