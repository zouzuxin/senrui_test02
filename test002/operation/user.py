import os

from api.user import user
from core.result_base import ResultBase


def post_api_token():
    # 获取登入接口的
    result = ResultBase()
    res = user.api_token()
    result.succes = False





if __name__ == '__main__':
    BASE_PATH =os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 使用os.path.join拼接进入指定文件
    data_file_path = os.path.join(BASE_PATH,"data\\all_storage\\api_token_storage","admin_token_storage.yml")
    print(data_file_path)
