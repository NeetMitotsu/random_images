import asyncio
import configparser
import logging
import random
from urllib.parse import urlparse

from flask import Flask
from flask import Response
from flask import make_response
from flask import request

import connetcion_pool as pool
from imgdata import Imgdata

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('./resource/profile.ini')
allowFiles = config.get('conf', 'imageAllowFiles')
def_category = config.get('conf', 'category')
whitelist = config.get('conf', 'whitelist')
server_port = config.getint('conf', 'server_port')

host = config.get('db', 'host')
port = config.getint('db', 'port')
user = config.get('db', 'user')
password = config.get('db', 'password')
charset = config.get('db', 'charset')
db = config.get('db', 'db')


async def init(loop_in):
    """
    初始化
    :return:
    """
    logging.info("program init......")
    await pool.create_pool(host=host, port=port, user=user, password=password,
                           charset=charset, db=db, loop=loop_in)
    # loop_tmp.run_forever()


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))


async def get_category_image(category: str = 'ACG', files_url: list = list()):
    """
    获取

    :param category: 类别
    :param files_url: 文件url
    :return:
    """
    data = await pool.select("SELECT photos.url, albums.title FROM ly__lychee_photos photos, " +
                             "ly__lychee_albums albums WHERE photos.public = 1 OR albums.visible = 1 " +
                             "AND photos.album = albums.id AND albums.title = %s", category)
    if data is None or len(data) < 1:
        return None
    for i in data:
        files_url.append(i)
    return files_url


# def get_files(category: str, allowFiles: str, files: list = list()):
#     """
#     获取图片文件名列表
#     """
#     path = os.path.abspath('.')
#     path = os.path.join(path, category)
#     if not os.path.isdir(path):
#         path = os.path.join(path, def_category)
#         if not os.path.isdir(path):
#             return None
#     for filePath in os.listdir(path):
#         path2 = os.path.join(path, filePath)
#         if os.path.isdir(filePath):
#             getfiles(path2, allowFiles, files)
#         else:
#             if re.match('.*(' + allowFiles + ')$', filePath, re.S):
#                 files.append(path2)
#     return files


def check_referer(url):
    """检查来源网址"""
    domain_list = whitelist.split(',')
    status = False
    # refer = ""
    if url in domain_list:
        status = True
    return status


@app.route('/image/<string:category>', methods=['GET', 'POST'])
def image(category):
    ref = request.headers.get('REFERER')
    status = False
    if ref:
        parse = urlparse(ref)
        status = check_referer(parse.netloc)
    if not status:
        logging.info("不支持的来源url：" + ref)
        return make_response('不支持的url', 404)
    # 没有相对路径， 返回空
    if not category:
        return make_response('资源未找到', 404)
    # 获取文件列表
    # file_list = get_files(category, allowFiles)
    # file_list = await get_category_image(category)
    file_list = get_category_image(category)
    # file_list = loop.run_until_complete(get_category_image(category))
    if not file_list:
        return make_response('资源未找到', 404)
    count = len(file_list)
    # 列表下标随机数
    rand = random.choice(range(count))
    img_path = file_list[rand]
    img = Imgdata(img_path['url'])
    info = img.data2img()
    # response.headers['content-type'] = info['content-type']
    return Response(info['data'], mimetype=info['content-type'])


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # try:
    # if not server_port:
    #     server_port = 6000
    print('启动')
    app.debug = True
    app.run(host='127.0.0.1')
    # finally:
    #     loop.close()
