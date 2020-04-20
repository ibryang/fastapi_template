from typing import Dict, List

from application.logger import get_service_logger
from model.user import User, UserUpdate

LOGGER = get_service_logger('USER')

users: Dict[int, any] = {
    1: UserUpdate(username='zhangsan', nickname="张三", age=13, password="admin"),
    2: UserUpdate(username='lisi', nickname="李四", is_active=False, password="admin"),
    3: UserUpdate(username='wanger1', nickname="王二1", age=22, password="admin"),
    4: UserUpdate(username='wanger2', nickname="王二2", age=22, password="admin"),
    5: UserUpdate(username='wanger3', nickname="王二3", age=22, password="admin"),
    6: UserUpdate(username='wanger4', nickname="王二4", age=22, password="admin"),
    7: UserUpdate(username='wanger5', nickname="王二5", age=22, password="admin"),
    8: UserUpdate(username='wanger6', nickname="王二6", age=22, password="admin"),
    9: UserUpdate(username='wanger7', nickname="王二7", age=22, password="admin"),
    10: UserUpdate(username='wanger8', nickname="王二8", age=22, password="admin"),
    11: UserUpdate(username='wanger9', nickname="王二9", age=22, password="admin"),
    12: UserUpdate(username='wanger10', nickname="王二10", age=22, password="admin"),
    13: UserUpdate(username='wanger11', nickname="王二11", age=22, password="admin"),
    15: UserUpdate(username='wanger12', nickname="王二12", age=22, password="admin"),
}


def get_users(skip: int = 0, limit: int = 10) -> List[User]:
    list_user = []
    for key, value in users.items():
        if key in list(users)[skip:skip + limit]:
            list_user.append(value)
    return list_user


def get_user_by_id(u_id: int) -> User:
    user = users.get(u_id, None)
    if user:
        return User(**user.dict())


def update_user(u_id: int, user_update: UserUpdate):
    if u_id in users.keys():
        users.update({u_id: user_update})
        return users[u_id]
