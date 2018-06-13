import mysql.connector
conn = mysql.connector.connect(user='root', password='root', host='localhost', port='3306', database='test')
cursor = conn.cursor()
cursor.execute("SELECT photos.* FROM ly__lychee_photos photos, " +
               "ly__lychee_albums albums WHERE photos.public = 1 OR albums.visible = 1 " +
               "AND photos.album = albums.id AND albums.title = %s", ('ACG',))
values = cursor.fetchall()
print(values)