import gzip
import xml.etree.ElementTree as ET
import os
import xml.dom.minidom
import csv
from tqdm import tqdm
import hashlib

# assign directory
directory = 'D:/gg'

# iterate over files in
# that directory
data =  []
no=0

def is_gzip_file(file_path):
    with open(file_path, 'rb') as f:
        magic_number = f.read(2)
        return magic_number == b'\x1f\x8b'

for filename in tqdm(os.listdir(directory)):

    if filename.endswith(".md5"):
        continue


    no +=1

    f = os.path.join(directory, filename)
    # checking if it is a file

    if os.path.isfile(f):
        if is_gzip_file(f):
            print(f"{f} is in gzip format.")
        else:
            continue
            print(f"{f} is not in gzip format.")

        #input= gzip.open(f, 'r')
        md5_hash = hashlib.md5()
        with open(f, "rb") as g:
            # Read and update hash in chunks of 4K
            for byte_block in iter(lambda: g.read(4096), b""):
                md5_hash.update(byte_block)
            print(md5_hash.hexdigest())
            with open(f"{f}.md5","r") as checkfile:
               text= checkfile.read()
               correctmd5=text.split()[1].strip()
               print(correctmd5)
               if correctmd5 == md5_hash.hexdigest():
                print("this file is matched")
               else:
                print(f"{f}is corrupt")
                g.close()
                with open("corrupt.txt", "a") as checkfile:
                    checkfile.write(f'{f}\n')
                os.remove(f)
            g.close()

        #with gzip.open(f, 'rb') as f:
            #compressed_content = f.read()

            #hash_object = hashlib.md5(compressed_content)
            #print(hash_object.hexdigest())











        # Update the hash object with the file contents








        # Create an MD5 hash object


        # Print the MD5 hash value

















