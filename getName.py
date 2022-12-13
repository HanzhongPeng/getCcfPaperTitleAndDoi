from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import main
import readCSV

class article(object):

    def getInfo(url,fileName):
        bsObj=main.getBsObj(url)
        # print(bsObj)
        fo=open(fileName+".txt","a+")
        for i in bsObj.find_all(class_="entry article"):
            title=i.find(class_="title")
            title=title.get_text()#提取文本
            print(title)
            doi=i.find("a")#找到规律，直接拿第一个链接就是了,doi值隐藏在这个链接之后
            doi=doi.get("href")
            doi=str(doi)
            print(doi)
            doi=doi.replace("http://","")#除去链接头
            doi=doi.replace("https://","")
            fo.writelines(title+"\n")
            fo.writelines(doi+"\n")
        fo.close()

if __name__ == '__main__':
    conf_url_list = readCSV.read_csv("conf_csv.csv")
    # print(conf_url_list)
    file_name_list = ["conf_A","conf_B","conf_C"]
    for eachLevel in range(3):
        for eachConf in range(len(conf_url_list[eachLevel])):
            article.getInfo(conf_url_list[eachLevel][eachConf]+"index.html",file_name_list[eachLevel])
