"""
-*- coding utf-8 -*-
@Time    :2023/12/3 17:27
@Author  :mila
@File    :test_api_a.py
@Software:PyCharm Community Edition
"""
import requests


def test_a():
    result = requests.get("http://www.baidu.com")
    assert result.status_code == 200
