import os
from shutil import rmtree

import requests


def downloader_file(download_link, save_path, retry_time=5, *args, **kwargs) -> bool:
    """
    下载文件
    :param str -> download_link: 下载链接
    :param str -> save_path: 保存路径
    :param int -> retry_time: 超时重试次数
    :return: bool -> 下载是否成功
    """
    if retry_time == 0:
        return False
    try:
        response = requests.get(download_link, timeout=5, *args, **kwargs)
        with open(save_path, 'wb') as f:
            f.write(response.content)
            f.flush()
        return True
    except Exception as e:
        retry_time -= 1
        if os.path.exists(save_path):
            os.remove(save_path)
        downloader_file(download_link, save_path, retry_time=retry_time)
        return False


def create_directory(path, delete_exist=False) -> None:
    """
    创建一个文件夹
    :param bool -> delete_exist: 当文件夹已存在时，是否删除重新创建
    :param str -> path: 创建的文件夹路径
    :return: None
    """
    if os.path.exists(path):
        if delete_exist:
            rmtree(path, ignore_errors=True)
    os.makedirs(path)
