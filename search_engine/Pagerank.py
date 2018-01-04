from bs4 import BeautifulSoup
from decimal import Decimal, getcontext
from multiprocessing import Process
import urllib2
import re
import os
import json
import time
#from mechanize import Browser#
#br = Browser()
# Ignore robots.txt
#br.set_handle_robots( False )


# ---- constants ---- #
starterConst = .25
dMulti = .8
dMinus = 1 - dMulti
threshold = 1500
urlList = ["https://en.wikipedia.org/wiki/Programming_language", "https://en.wikipedia.org/wiki/Processor", "https://en.wikipedia.org/wiki/Informatics"]
urlMatrix = []
urlIndices = {}
urlDict = {}
pageRankScore = {}
indexMapper	= ""
dirPath = ""

def createUrlDict2():
    global indexMapper
    indexMapper = 'index.txt'
    indexFile = open(indexMapper, 'w')
    global dirPath
    dirPath = "CrawledPages"
    try:
        os.makedirs(dirPath)
    except OSError:
        if not os.path.isdir(dirPath):
            raise
    i = 0
    tempurlDict = {}
    tempurlDict[urlList[0]] = True
    for url in urlList:
        counter = len(urlIndices)
        if counter >= threshold: break
        if url not in urlIndices: urlIndices[url] = counter
        if url not in urlDict: urlDict[url] = []
        fileName = "urlpage" + str(counter) + ".html"
        try:
            req = urllib2.Request(url, headers={ 'User-Agent': 'IUB-I427-FinalProject' })
            response = urllib2.urlopen(req).read()
            #response = urllib2.urlopen(url) #.read()
            soup = BeautifulSoup(response, "lxml")
        except:
            continue
        indexFile.write(fileName + "\t" + url + "\n")
        completeName = os.path.join(os.getcwd() + "/" + dirPath, fileName)
        f = open(completeName,"w")
        f.write(response)
        f.close()

        for link in soup.findAll('a', href=True):
            _link = link['href']
            if i >= threshold or _link in urlIndices: break
            print(_link)
            if _link[:5] == "/wiki":
                _link = "https://en.wikipedia.org" + _link
                print(_link)
                if _link not in urlIndices and _link not in tempurlDict:
                    tempurlDict[_link] = True
                    urlList.append(_link)
                if _link not in urlDict[url]: urlDict[url].append(_link)
                i += 1
        i += 1
        print(i)
tempurlDict = {}
urlList3 = []

def createMatrix():
    listSize = len(urlList)
    global urlMatrix
    urlMatrix = [ [ 0 for i in range(listSize) ] for j in range(listSize) ]
    for node in urlDict:
        row = urlIndices[node]
        for url in urlDict[node]:
            col = urlIndices[node]
            try:
                urlMatrix[row][col] = 1
            except:
                print(str(row) + " " + str(col))
    # for row in urlMatrix:
        # print(row)

def calcInLinks(url):
    idx = urlIndices[url]
    count = 0
    for i in range(0, len(urlMatrix)):
        if urlMatrix[i][idx] == 1:
            count += 1
    return count
def calcOutLinks(url):
    return len(urlDict[url]) if (len(urlDict[url]) != 0) else 10
def calcMarkovChain(url):
    getcontext().prec = 10
    iLinks = calcInLinks(url)
    oLinks = calcOutLinks(url)
    if oLinks == 0:
        return .01
    return float(iLinks) / float(oLinks)
def fillPageRank():
    for url in urlList:
        pageRankScore[url] = float(starterConst)

    for url in urlList:
        pageRankScore[url] += float(dMinus) + float(dMulti) * float(calcMarkovChain(url))

    for key, val in pageRankScore.items():
        pageRankScore[url] = str(float(val))

    with open('pagerank_scores.txt', 'w') as prfile:
       prfile.write(json.dumps(pageRankScore))
       prfile.close()
def pageRank():
    createUrlDict2()
    createMatrix()
    fillPageRank()
