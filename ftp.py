import fnmatch
from ftplib import FTP
import ftplib
ftp_server = ftplib.FTP("ftp.ncbi.nlm.nih.gov", "anonymous", "wanhoyinjoshua@yahoo.com")
# force UTF-8 encoding
ftp_server.encoding = "utf-8"
#if username and password is required.
ftp_server.cwd('/pubmed/baseline')
ftp_server.dir()
files = ftp_server.nlst()
print(files)
for file in files:

    if fnmatch.fnmatch(file, '*.xml.gz'):   #To download specific files.
        print("Downloading..." + file)

        try:
            ftp_server.retrbinary("RETR " + file ,open("C:/Users/wanho/PycharmProjects/pubmedscraper/files" + file, 'wb').write)

        except:    # To avoid EOF errors.

            pass

ftp_server.close()


# if you have to change directory on FTP server.



