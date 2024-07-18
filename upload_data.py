from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file_path = '/home/devops/Desktop/mac_address.txt'
file_name = 'mac_address-2.txt'

gfile = drive.CreateFile({"title": file_name})

gfile.SetContentFile(file_path)

gfile.Upload()

print('Uploaded file with ID %s' % gfile.get('id'))
