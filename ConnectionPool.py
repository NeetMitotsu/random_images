import mysql.connector
conn = mysql.connector.connect(user='jty', password='jty_1994127', host='67.218.132.112', port='3306', database='lychee')
cursor = conn.cursor()
cursor.execute("SELECT photos.* FROM ly__lychee_photos photos, " +
               "ly__lychee_albums albums WHERE photos.public = 1 OR albums.visible = 1 " +
               "AND photos.album = albums.id AND albums.title = %s", ('ACG',))
values = cursor.fetchall()
print(values)