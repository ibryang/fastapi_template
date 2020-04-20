import logging


def get_controller_logger(name):
    """
    获取控制器logger
    :param name: controller name
    :return: controller logger
    """
    return logging.getLogger('CONTROLLER_' + str(name).upper())


def get_middleware_logger(name: str):
    """
    获取中间件logger
    :param name: middleware name
    :return: middleware logger
    """
    return logging.getLogger('MIDDLEWARE_' + str(name).upper())


def get_service_logger(name: str):
    """
    获取server logger
    :param name: service name
    :return: service logger
    """
    return logging.getLogger('SERVICE_' + str(name).upper())
