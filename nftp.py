import fnmatch
from ftplib import FTP
import ftplib
import io
import os
import requests
from tqdm import tqdm
import os
import time
import gzip
import xml.etree.ElementTree as ET
import csv
directory = "D:/gg/"

filenames = os.listdir(directory)
print(filenames)
ftp_server = ftplib.FTP("ftp.ncbi.nlm.nih.gov", "anonymous", "wanhoyinjoshua@yahoo.com",timeout=300)
# force UTF-8 encoding
ftp_server.encoding = "utf-8"

#if username and password is required.
ftp_server.cwd('/pubmed/baseline')
ftp_server.dir()
files = ftp_server.nlst()
print(files)

local_path = r'D:/gg/'  # change this to the path of your choice

import re



for file in files:

    if file in filenames:
        print("skip")
        continue





    remote_file_path = file
with ftplib.FTP("ftp.ncbi.nlm.nih.gov", "anonymous", "wanhoyinjoshua@yahoo.com",timeout=30) as ftp:
    # Download the file to a BytesIO object
    ftp_server.cwd('/pubmed/baseline')
    for file in files:

        if file in filenames:
            print("skip")
            continue

        file_bytes = io.BytesIO()
        local_file = open(local_path + file, 'wb')

        try:
            print(f"downloading {file}")
            ftp_server.retrbinary('RETR ' + file, local_file.write)
            print(f"completed download {file}")
        except Exception as e:
            print('Error during download:', e)
            local_file.close()
            continue

        time.sleep(2)

        local_file.close()





            # Update the hash object with the file contents











ftp_server.quit()


# Disconnect from FTP server



