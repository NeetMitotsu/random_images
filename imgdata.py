import magic
import os

class Imgdata(object):
	__slots__ = ('__imgsrc', '__imgdata', '__imgform')
	"""docstring for Imgdata"""
	def __init__(self, imgsrc):
		super(Imgdata, self).__init__()
		self.__imgsrc = imgsrc
		filesize = os.path.getsize(self.__imgsrc)
		with open(self.__imgsrc, 'rb') as rb:
			#保存字节数组数据
			self.__imgdata = rb.read(filesize)
		# self.__imgdata = imgdata
		#初始化数据，保存imgform（mime信息即content-type）
		mime = magic.Magic(mime=True)
		self.__imgform = mime.from_file(imgsrc)

	# def img2data():
	# 	# self._imgform(self.__imgsrc)
	# 	filesize = os.path.getsize(self.__imgsrc)
	# 	with open(self.__imgsrc, 'rb') as rb:
	# 		self.__imgdata = rb.read(filesize)

	def data2img(self):
		"""
		返回文件content-type与字节数组data 字典

		:return dict
		"""
		info = {};
		info['content-type'] = self.__imgform
		info['data'] = self.__imgdata
		return info
		

	# def _imgform():
	# 	mime = magic.Magic(mime=True)
	# 	self.__imgform = mime.from_file(self.__imgsrc)

	@property
	def imgsrc(self):
		return self.__imgsrc

	@imgsrc.setter
	def imgsrc(self, value):
		self.__imgsrc = value

	@property
	def imgdata(self):
		return self.__imgdata

	@imgdata.setter
	def imgdata(self, value):
		self.__imgdata = value

	@property
	def imgform(self):
		return self.__imgform

	@imgform.setter
	def imgform(self, value):
		self.__imgform = value
