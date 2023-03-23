# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.by import By


import csv




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = webdriver.Chrome()
    #loop through year
    for z in range(2019,2023):
        driver.get(
            f"https://pubmed.ncbi.nlm.nih.gov/?term=physiotherapy&filter=years.{str(z)}-{str(z)}&size=200&page={1}")
        #find max page no and convert from string to num and back to string
        limitpage = driver.find_element(By.XPATH, "//label[@class='of-total-pages']").text
        limitno = int(limitpage.split(" ")[1])
        print(limitno)
        year=str(z)
        engine="pubmed"
        #loop through pages
        for w in range(1, limitno+1):
            masterlist=[]
            driver.get(
                f"https://pubmed.ncbi.nlm.nih.gov/?term=physiotherapy+NOT+%28review%5BFilter%5D+OR+editorial%5BFilter%5D%29&filter=years.{year}-{year}&size=200&page={w}"
                )
        #xpath for author name =//article[1]//div[@class="docsum-wrap"]//div[@class="docsum-content"]//div[@class="docsum-citation full-citation"]//span[@class="docsum-authors full-authors"]
        #xpath for article id in pub med = //article[1]//div[@class="docsum-wrap"]//div[@class="docsum-content"]//div[@class="docsum-citation full-citation"]//span[@class="citation-part"]//span[@class="docsum-pmid"]
            #loop through 200 options as that is the display setting , i set it as 200 items on the screen as per url
            for i in range(1, 201):
                try:
                    #just finding a dom element
                    authors = driver.find_element(By.XPATH,"(//article)[{0}]//div[@class='docsum-wrap']//div[@class='docsum-content']//div[@class='docsum-citation full-citation']//span[@class='docsum-authors full-authors']".format(i)).text
                    authorno = len(authors.split(","));
                except:
                    authors="not found"
                    continue
                try:
                    pubmedid = driver.find_element(By.XPATH,
                                                   "(//article)[{0}]//div[@class='docsum-wrap']//div[@class='docsum-content']//div[@class='docsum-citation full-citation']//span[@class='citation-part']//span[@class='docsum-pmid']".format(
                                                       i)).text
                    #i determine author no by lookign at , and then I split them up into an array based on that, so three items in the array tells me there are three authors


                except:



                    pubmedid="not found"
                    continue



                row=[engine,year,pubmedid,authors,authorno]
                with open(f"pubmed-{year}mm.csv", 'a', encoding='UTF8', newline='') as f:
                    # using csv.writer method from CSV package
                    write = csv.writer(f)

                    write.writerow(row)


            #not doing much but just scrolling down, does not do much really , as sometimes when you scrap websites, this will help you not getting blocked/ banned
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")





        # See PyCharm help at https://www.jetbrains.com/help/pycharm/
