import xcolor

from application.controller import success
from application.logger import get_controller_logger
from fastapi import APIRouter, UploadFile, File
import os

app_name = os.getenv('APP_NAME')
app_version = os.getenv('VERSION')
app_description = os.getenv('DESCRIPTION')

router = APIRouter()

LOGGER = get_controller_logger('BASE')


@router.get('/')
async def index():
    return success('success')


@router.get('/appinfo')
def health_check():
    return success({
        'name': app_name,
        'version': app_version,
        'description': app_description
    })


@router.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    content = await file.read()
    LOGGER.info('收到文件 %s:\n' % filename)
    return success({
        'filename': filename,
        'contentType': file.content_type,
        'size': len(content)
    })
