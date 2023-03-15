import os

import requests

from common.read_data import data
from core.result_client import RestClient
from core.result_base import ResultBase

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]

class User(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    def api_token(self, **kwargs):
        # {
        return self.post("/api/user/connect/token", **kwargs)

user = User(api_root_url)

if __name__ == '__main__':
    datas = {'client_id': 'pcclient', 'client_secret': 'HdiS&Pc!', 'grant_type': 'HDIS', 'scope': 'api1',
             'username': 'admin', 'password': 'E10ADC3949BA59ABBE56E057F20F883E',
             'instid': '714DBCB5-9C8F-4048-8AAF-DA7549BBF5C0'}
    header = {
        "Accept":"application/json, text/plain, */*",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"keep-alive",
        "Content-Length":"198",
        "Content-Type":"application/json",
        "Host":"dev.api.senruisoft.com",
        "Origin":"http://dev.pad.senruisoft.com",
        "Referer":"http://dev.pad.senruisoft.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = user.api_token(json = datas,headers = header)
    print(res.json())
