from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Image(Base):
    __tablename__='ly__lychee_photos'
    id = Column(String(14), primary_key=True)
    title = Column(String(100))
    description = Column(String(1000))
    url = Column(String(100))
    tags = Column(String(1000))
    public = Column(String(1))
    type = Column(String(10))
    width = Column(String(11))
    height = Column(String(11))
    size = Column(String(20))
    iso = Column(String(15))
    aperture = Column(String(20))
    make = Column(String(50))
    model = Column(String(50))
    shutter = Column(String(30))
    focal = Column(String(20))
    takestamp = Column(String(11))
    star = Column(String(1))
    thumbUrl = Column(String(37))
    album = Column(String(14))
    checksum = Column(String(40))
    medium = Column(String(1))
    position = Column(String(1))

engine = create_engine('mysql+pymysql://root:rootpass@localhost/test')
DBSession = sessionmaker(bind=engine)

session = DBSession()
image = session.query(Image).filter(Image.id == '1').one()
print(type(image))
print(image.url)
session.close()