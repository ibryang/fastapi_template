import xcolor
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from application import router
import os
from typing import Dict, Any

"""使用 os.getenv() 在dev.cfg或prod.cfg中获取ENV变量"""
env: str = os.getenv('ENV')
app_name: str = os.getenv('APP_NAME')
description: str = os.getenv('DESCRIPTION')
version: str = os.getenv('VERSION')
fastapi_cfg: Dict[str, Any] = {
    'debug': env != 'prod',
    'title': app_name,
    'description': description,
    'version': version,
}

"""init app"""
app = FastAPI(**fastapi_cfg)
app.mount("/static", StaticFiles(directory="static"), name="static")
router.register_controllers(app)
router.register_middlewares(app)
