# start-fastapi

基于fastapi的轻量级Web服务器框架

基于[FastAPI](https://github.com/tiangolo/fastapi)的简易Web后端开发框架

定位是快速实现效率工具/轻量级后端，比如xx机器人、xx数据处理服务器等，暂未有接一堆中间件SDK的计划

整个框架在fasiapi基础上梳理了目录结构、配置等容易踩坑的内容，这样业务就能基本专心写crud了

## References

一般的文档在这3个地方找就ok了

- [FastAPI](https://fastapi.tiangolo.com/)
- [Starlette](https://www.starlette.io/)
- [Uvicorn](https://www.uvicorn.org/)

## Requirements

- python 3.6+ (for static typing check)
- `pip3 install -r ./requirements.txt` (using venv is recommended)
- idea/pycharm (optional but recommended)

## Structure

非常经典的的洋葱圈模型

- 应用程序：应用程序模块（控制器，中间件，服务，路由器等）的基本api
- 配置：配置文件（json）
- 控制器：具有路由器回调的控制器模块
- 中间件：中间件
- 模型：用于键入检查的内部数据模型
- 服务：服务库
- 测试：自定义测试脚本
- main.py：服务器条目

## Configuration

首先让我们看一下初始化应用程序的步骤：

- 用户运行命令`./venv/bin(Scripts)/python main.py（dev/prod）`
- uvicorn在config/uvicorn/dev（prod）.json`中使用cfg启动`app.py`/uvicorn/logger.json`将成为uvicorn的记录器cfg
- 应用程序将`config/dev（prod）.cfg`加载为env配置
- 应用程序注册控制器和中间件，从而启动所有模块的导入

所以我们需要这样的参考：

有关配置应用程序和记录器json的参考：
- [uvicorn settings](https://www.uvicorn.org/settings/)
- [config.py](https://github.com/encode/uvicorn/blob/master/uvicorn/config.py)

有关配置dev.cfg或prod.cfg的参考：

- [python-dotenv](https://github.com/theskumar/python-dotenv)

## Example

以整个初始项目为例，从cd到根目录并运行`./script/dev.sh`启动服务器。

如果您想编写自己的逻辑，则：

- 在`config/router.py`中添加控制器路由，并在./controller`中添加相应的回调-根据您的控制器，在`./service`中添加唯一或多实例服务-在`./model中添加数据模型用于服务和控制器的`
- 必要时添加中间件，请参见[fastapi中间件]（https://fastapi.tiangolo.com/tutorial/middleware/）
- 如果需要记录，请从application.xxx调用get_logger func到获取记录器
- cd到根目录并运行`python3./main.py`

全局性质的对象尽可能放到application中，unique service跟多实例的service都放到service下，后者用class封装就好了

### Requests and Responses

所有已处理的请求的状态码为200

如果未成功处理请求，则用户应在application.controller中调用error来包装响应正文 否则，在application.controller中调用success来包装响应正文请求主体架构是在用户上定义的，请查看[FastAPI请求正文]（https://fastapi.tiangolo.com/tutorial/body/）以获取详细信息响应正文的基本架构为：

```text
{
  "success": bool,
  "message": string,
  "code": int,
  "data": any,
}
```

所有能处理走到逻辑的都返回200，由success和code控制处理结果。不能处理或处理出exception的，由fastapi底层代理

### export your requirements

在进行协作时，每个成员应根据需要同步库

run `pip freeze > requirements.txt` or `./script/export.sh` (if venv dir included) before commit

## Deployment

run `./script/pack.sh` to pack the project into `./build/start-fastapi.tar.gz`

if docker deployment is needed, take reference to `./build/Dockerfile`

## TODO

- testing
- RBAC
