import magic
import os


class Imgdata(object):
    """docstring for Imgdata"""

    __slots__ = ('__imgsrc', '__imgdata', '__imgform')

    def __init__(self, imgsrc):
        super(Imgdata, self).__init__()
        self.__imgsrc = imgsrc
        filesize = os.path.getsize(self.__imgsrc)
        with open(self.__imgsrc, 'rb') as rb:
            # 保存字节数组数据
            self.__imgdata = rb.read(filesize)
        # self.__imgdata = imgdata
        # 初始化数据，保存imgform（mime信息即content-type）
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

        :return: keys: content-type, data
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

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self, value):
        self.__tags = value

    @property
    def public(self):
        return self.__public

    @public.setter
    def public(self, value):
        self.__public = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def iso(self):
        return self.__iso

    @iso.setter
    def iso(self, value):
        self.__iso = value

    @property
    def aperture(self):
        return self.__aperture

    @aperture.setter
    def aperture(self, value):
        self.__aperture = value

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, value):
        self.__make = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def shutter(self):
        return self.__shutter

    @shutter.setter
    def shutter(self, value):
        self.__shutter = value

    @property
    def focal(self):
        return self.__focal

    @focal.setter
    def focal(self, value):
        self.__focal = value

    @property
    def takestamp(self):
        return self.__takestamp

    @takestamp.setter
    def takestamp(self, value):
        self.__takestamp = value

    @property
    def star(self):
        return self.__star

    @star.setter
    def star(self, value):
        self.__star = value

    @property
    def thumbUrl(self):
        return self.__thumbUrl

    @thumbUrl.setter
    def thumbUrl(self, value):
        self.__thumbUrl = value

    @property
    def album(self):
        return self.__album

    @album.setter
    def album(self, value):
        self.__album = value

    @property
    def checksum(self):
        return self.__checksum

    @checksum.setter
    def checksum(self, value):
        self.__checksum = value

    @property
    def medium(self):
        return self.__medium

    @medium.setter
    def medium(self, value):
        self.__medium = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
