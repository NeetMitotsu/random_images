from flask import Flask
from flask import request
from flask import Response
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
imageManagerListPath = config.get('conf', 'imageAllowFiles')
basePath = config.get('conf', 'basePath')
category = config.get('conf', 'category')


@app.route('/image/<string:category>', methods=['GET', 'POST'])
def image(category):
    # 没有相对路径， 返回空
    if not category:
        return Response(status=404)
    # 获取文件列表
    filelist = getfiles(category, allowFiles)
    if not filelist:
        return Response(status=404)
    count = len(filelist)
    # 列表下标随机数
    rand = random.choice(range(count))
    imgpath = filelist[rand]
    img = Imgdata(imgpath)
    info = img.data2img()
    # response.headers['constent-type'] = info['content-type']
    return Response(info['data'], mimetype=info['content-type'])


def getfiles(category: str, allowFiles: str, files: list = list()):
    """
    获取图片文件名列表
    """
    path = os.path.abspath('.')
    path = os.path.join(path, basePath, category)
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


def checkReferer(url, domainList=['www.yuudati.com', 'www.jty127.com']):
    """检查来源网址"""
    status = False
    refer = ""
    if refer in domainList:
        status = True
    return status


if __name__ == '__main__':
    app.run('127.0.0.1', debug=True)
