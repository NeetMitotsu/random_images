from flask import Flask
from flask import request
from flask import Response
from flask import make_response
import json
import time
from urllib.parse import urlparse
from imgdata import Imgdata

import os
import re
import configparser
import random

app = Flask(__name__)
# print(os.path.abspath('.'))
config = configparser.ConfigParser()
config.read('./resource/profile.ini')
allowFiles = config.get('conf', 'imageAllowFiles')
basePath = config.get('conf', 'basePath')
def_category = config.get('conf', 'category')
whitelist = config.get('conf', 'whitelist')
port = config.getint('conf', 'port')

def getfiles(category: str, allowFiles: str, files: list = list()):
    """
    获取图片文件名列表
    """
    path = os.path.abspath('.')
    path = os.path.join(path, basePath, category)
    if not os.path.isdir(path):
        path = os.path.join(path, basePath, def_category)
        if not os.path.isdir(path):
            return None
    for filePath in os.listdir(path):
        path2 = os.path.join(path, filePath)
        if os.path.isdir(filePath):
            getfiles(path2, allowFiles, files)
        else:
            if re.match('.*(' + allowFiles + ')$', filePath, re.S):
                files.append(path2)
    return files


def checkreferer(url):
    """检查来源网址"""
    domainlist = whitelist.split(',')
    status = False
    refer = ""
    if refer in domainlist:
        status = True
    return status


@app.route('/image/<string:category>', methods=['GET', 'POST'])
def image(category):
    ref = request.headers.get('REFERER')
    status = False
    if ref:
        parse = urlparse(ref)
        status = checkreferer(parse.netloc)
    if not status:
        return make_response('不支持的url', 404)
    # 没有相对路径， 返回空
    if not category:
        return make_response('资源未找到', 404)
    # 获取文件列表
    filelist = getfiles(category, allowFiles)
    if not filelist:
        return make_response('资源未找到', 404)
    count = len(filelist)
    # 列表下标随机数
    rand = random.choice(range(count))
    imgpath = filelist[rand]
    img = Imgdata(imgpath)
    info = img.data2img()
    # response.headers['constent-type'] = info['content-type']
    return Response(info['data'], mimetype=info['content-type'])


if __name__ == '__main__':
    if not port:
        port = 6000
    app.run('0.0.0.0', port=port, debug=False)
