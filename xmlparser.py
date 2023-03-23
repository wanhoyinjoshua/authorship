import gzip
import xml.etree.ElementTree as ET
import os
import xml.dom.minidom
import csv
from tqdm import tqdm
# assign directory
directory = 'files'

# iterate over files in
# that directory
data =  []
no=0
for filename in tqdm(os.listdir(directory)):
    no +=1


    f = os.path.join(directory, filename)
    # checking if it is a file
    print(f)

    if os.path.isfile(f):
        input = gzip.open(f"{f}", 'r')
        for event, elem in ET.iterparse(input, events=('start', 'end')):
            if event == 'start':
                if elem.tag == "PubmedArticle":
                    pub = {}  # INITIALIZE ARTICLE DICT

                if elem.tag == 'PMID':
                    pub["PMID"] = elem.text
                    pub["PublicationType"] = []

                elif elem.tag == 'ArticleTitle':
                    pub["title"] = elem.text







                elif elem.tag == 'PubDate':
                    try:

                        if "-" in elem[0].text:
                            year= elem[0].text.split(" ")
                            pub["publicationdate"] = year[0]

                        else:
                            pub["publicationdate"] = elem[0].text


                    except:
                        pub["publicationdate"] = "N/A"






                elif elem.tag == 'PublicationType':
                    pub["PublicationType"].append(elem.text)


                elif elem.tag == 'AuthorList':
                    authorcount=0
                    authortext=[]
                    for author in elem:
                        authorcount+=1
                        for child in author:
                            if child.tag=='LastName':

                                authortext.append(child.text)
                    pub["Authors"] = authorcount
                    pub["names"] = authortext











            if event == 'end':
                if elem.tag == "PubmedArticle":
                    pub["Source"] = filename
                    try:
                        with open("D:/pubmedscrapedata/data.csv", 'a', encoding='UTF8', newline='') as f:
                            # using csv.writer method from CSV package
                            resultList = list(pub.values())
                            write = csv.writer(f)

                            write.writerow(resultList)
                    except:
                        with open(f"D:/pubmedscrapedata/data_{no}.csv", 'a', encoding='UTF8', newline='') as f:
                            # using csv.writer method from CSV package
                            resultList = list(pub.values())
                            write = csv.writer(f)

                            write.writerow(resultList)


            elem.clear()
















