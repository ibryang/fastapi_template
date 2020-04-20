from typing import Dict, Any
import uvicorn
import sys
import getopt
import os
import json

import xcolor

"""
Start_FastApi的主要输入项，
用于UVICORN而不是FASTAPI 
APP的加载配置只是需要在config/app中修改配置
"""

# load application config
_CONFIG: Dict[str, Any] = dict()
_CONFIG_ROOT: str = 'config/uvicorn'
_DEV_CONFIG_PATH: str = 'dev.json'
_PROD_CONFIG_PATH: str = 'prod.json'
_APP_MODE: str = 'dev'
_APP_KEY: str = 'app'
_LOGGER_KEY: str = 'logger'
_BANNER = """ _____ ______ ______  _     _ 
(_____|____  (_____ \| |   | |
   _   ____)  )____) ) |___| |
  | | |  __  (_____ ( \_____/ 
 _| |_| |__)  )    | |  ___   
(_____)______/     |_| (___) 
"""


def _print(*args):
    print(*args, file=sys.stderr)


def _get_cfg_json(*args) -> Dict:
    """
    从特定的配置路径加载json配置
    :param args: path
    :return: json config
    """
    return json.loads(open(os.path.join(_CONFIG_ROOT, *args)).read())


def _load_cfg(mode: str):
    """
    从路径加载配置到_CONFIG
    :param mode: application mode (dev or prod)
    :return: None
    """
    # 获取应用模型
    if not mode == 'prod' and not mode == 'dev':
        raise Exception('Unknown application mode')
    global _CONFIG
    global _APP_MODE
    _APP_MODE = mode
    if _APP_MODE == 'dev':
        _CONFIG = _get_cfg_json(_DEV_CONFIG_PATH)
    else:
        _CONFIG = _get_cfg_json(_PROD_CONFIG_PATH)
    # 检查是否加载了应用程序配置
    if _APP_KEY not in _CONFIG.keys():
        raise Exception('Failed to load application config')
    # 加载日志配置信息
    if _LOGGER_KEY in _CONFIG.keys():
        log_config = None
        raw_logger_cfg = _CONFIG[_LOGGER_KEY]
        if isinstance(raw_logger_cfg, dict):
            if 'path' in raw_logger_cfg.keys():
                log_cfg_path = str(raw_logger_cfg['path'])
                try:
                    log_config = _get_cfg_json(log_cfg_path)
                except Exception as e:
                    _print('Failed to load logger config at %s! %s' % (log_cfg_path, e))
            if not log_config and 'content' in raw_logger_cfg.keys():
                log_config = raw_logger_cfg['content']
        if log_config and isinstance(log_config, dict):
            _CONFIG[_APP_KEY]['log_config'] = log_config


def main():
    # 获取应用配置
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'e:', ['env='])  # no error handling here
    except getopt.GetoptError as e:
        raise e
    env = 'dev'
    for o, a in opts:
        if o == '-e':
            if a == 'prod':
                env = 'prod'
    _load_cfg(env)
    if not _CONFIG:
        raise Exception('Failed to load config!')
    xcolor.blue1.print(_BANNER)
    # 运行应用
    uvicorn.run('app:app', **_CONFIG[_APP_KEY])


if __name__ == '__main__':
    main()
