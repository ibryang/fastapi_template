from controller import base, item, user
from middleware import connection
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def register_controllers(app: FastAPI) -> None:
    """
    将控制器回调注册到路由器注：/docs和/redoc是fastapi的内部路由器
    :param app: fastapi app
    :return: None
    """
    app.include_router(base.router)
    app.include_router(item.router, prefix='/items', tags=['items'])
    app.include_router(user.router, prefix='/users', tags=['users'])


def register_middlewares(app: FastAPI) -> None:
    """
    注册中间件
    :param app: fastapi app
    :return: None
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.middleware('http')(connection.calc_time)
