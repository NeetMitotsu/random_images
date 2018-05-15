from flask import Flask
from flask import request
from flask import make_response
import json
import time
from urllib.parse import urlparse

import os
import re

app = Flask(__name__)

@app.route('/image')
def image():
	headers = request.headers
	# 来源
	referer = headers['referer']
	if referer:
		refererhost = urlparse(referer)
		host = refererhost.netloc.lower()
		status = checkReferer(host)
	else:
		pass


def getfiles(dirpath:str, allowFiles:list, files:list = list()):
	"""
	获取图片文件名列表
	"""
	if not os.path.isdir(dirpath):
		return None;
	if dirpath[-1] != '\\':
		dirpath = dirpath + '\\'
	for filePath in os.listdir(dirpath):
		path2 = os.path.join(dirpath, filePath)
		if os.path.isdir(filePath):
			getfiles(path2, allowFiles, files)
		else:
			# "/\.(" . $allowFiles . ")$/i"
			if re.match(".(".join(allowFiles).join(")$/i"), filePath):
				files.append(path2)
	return files

def checkReferer(url, domainList = ['www.yuudati.com','www.jty127.com']):
	"""检查来源网址"""
	status = False
	refer = ""
	if refer in domainList:
		status = True
	return status


