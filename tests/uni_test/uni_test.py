"""
-*- coding utf-8 -*-
@Time    :2023/12/3 18:35
@Author  :mila
@File    :uni_test.py
@Software:PyCharm Community Edition
"""
import json

from src.main import get_file_with_path


def test_file():
    file_list = get_file_with_path(r"E:\Download\code_edit\December\Dudod\src")
    json_data = json.dumps(file_list)
    assert len(file_list) == 3
    assert "main.py" in json_data
