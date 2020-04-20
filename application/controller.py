from typing import Any, Dict


def success(data: Any = None, msg: str = 'success') -> Dict[str, Any]:
    """
    产生成功的响应
    :param data: data
    :param msg: message
    :return: json resp body
    """
    return {
        'data': data,
        'success': True,
        'message': msg,
        'code': 0,
    }


def error(data: Any = None, msg: str = '', code: int = -1) -> Dict[str, Any]:
    """
    generate error response body with external status code 200
    :param data: data
    :param msg: message
    :param code: user defined (not http) status code
    :return: json resp body
    """
    return {
        'data': data,
        'success': False,
        'message': msg,
        'code': code,
    }
