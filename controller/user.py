import aiohttp
import requests
from fastapi import APIRouter

from application.controller import success, error
from application.logger import get_controller_logger
from model.user import UserUpdate, User
from service import user as user_service
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

router = APIRouter()

LOGGIN = get_controller_logger("USER")


@router.get('/')
async def get_users(skip: int = 0, limit: int = 10):
    return success(user_service.get_users(skip, limit))


@router.get('/video')
async def get_videos():
    url = 'https://mi180.com/api_taiyang.php?pt=taiyang_shibajin'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    response = requests.get(url, verify=False, headers=headers)
    html = response.text()
    return success(msg='success', data=html)


@router.get('/{u_id}')
async def get_user(u_id: int):
    user = user_service.get_user_by_id(u_id)
    if user:
        return success(user)
    return error(msg='该用户不存在')


@router.put('/{u_id}')
def update_user(u_id: int, user: UserUpdate):
    user = user_service.update_user(u_id, user)
    if user:
        return success(user)
    return error(msg='该用户不存在')
