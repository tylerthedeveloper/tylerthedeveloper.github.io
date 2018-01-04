from bs4 import BeautifulSoup
from decimal import Decimal, getcontext
from multiprocessing import Process
import urllib2
import re
import os
import json
import time
#from mechanize import Browser
#br = Browser()
# Ignore robots.txt
#br.set_handle_robots( False )


# ---- constants ---- #
starterConst = .25
dMulti = .8
dMinus = 1 - dMulti
threshold = 10
urlList = ["http://gpsonline.brandeis.edu/", "https://www.indiana.edu/", "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States", "https://www.nytimes.com/", "https://bulbapedia.bulbagarden.net/wiki/Main_Page", "http://www.espn.com/"]
urlMatrix = []
urlIndices = {}
urlDict = {}
pageRankScore = {}
indexMapper	= ""
dirPath = ""

def createUrlDict():
    listSize = 20
    urlMatrix = [ [ 0 for i in range(listSize) ] for j in range(listSize) ]
    i = 0
    for url in urlList:
        counter = len(urlIndices)
        if counter >= threshold: break
        urlDict[url] = []
        if url not in urlIndices:
            urlIndices[url] = counter
        try:
            page = urllib2.urlopen(url)
            soup = BeautifulSoup(page, "lxml")
        except:
                continue
        for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
            counter = len(urlIndices)
            _link = link['href']
            if counter >= threshold or _link in urlIndices: break
            urlMatrix[i][counter] = 1
            urlDict[url].append(_link)
            urlList.append(_link)
        i += 1


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

        for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
            _link = link['href']
            if i >= threshold or _link in urlIndices: break
            if _link not in urlIndices and _link not in tempurlDict:
                tempurlDict[_link] = True
                urlList.append(_link)
            if _link not in urlDict[url]: urlDict[url].append(_link)
            i += 1
        i += 1
tempurlDict = {}
urlList3 = []
def multiProcess(seed):
    global indexMapper
    global dirPath
    global indexMapper
    indexMapper = 'index.txt'
    indexFile = open(indexMapper, 'w')
    dirPath = "CrawledPages"
    urlList3.append(seed)

    curCount = 0
    createUrlDict3(seed, curCount)
    for _url in urlList3:
        curCount += 1
        if "www" in _url:
            bucket = _url[_url.find(".") + 1]
        else:
            bucket = _url[_url.find("//") + 2]
        bucket = bucket.upper()
        if bucket <= 72:
            a = Process(target=createUrlDict3, args=(_url,curCount))
            a.start()
        elif bucket <= 78:
            a = Process(target=createUrlDict3, args=(_url,curCount))
            a.start()
        elif bucket <= 85:
            a = Process(target=createUrlDict3, args=(_url,curCount))
            a.start()
        else:
            a = Process(target=createUrlDict3, args=(_url,curCount))
            a.start()

        urlList3.append(a.exitcode)
#Not Used
def createUrlDict3(curUrl, curCount):
    #global urlIndices
    global urlList3
    global indexMapper
    indexMapper = 'index.txt'
    indexFile = open(indexMapper, 'a')
    global dirPath
    #dirPath = "CrawledPages"
    try:
        os.makedirs(dirPath)
    except OSError:
        if not os.path.isdir(dirPath):
            raise

    #counter = len(urlIndices)
    counter = curCount
    if counter >= threshold: return
    tempurlDict[curUrl] = True
    #if curUrl not in urlIndices:
        #print "b4 count  " + str(curCount) + " " + curUrl
    urlIndices[curUrl] = counter
    if curUrl not in urlDict: urlDict[curUrl] = []

    #print "after count  " + str(len(urlIndices))
    fileName = "urlpage" + str(counter) + ".html"
    try:
        #print curUrl
        page = urllib2.urlopen(curUrl)
        soup = BeautifulSoup(page, "lxml")
    except:
        print("hi")
    indexFile.write(fileName + "\t" + curUrl + "\n")
    #response = urllib2.urlopen(curUrl).read()
    response = page.read()
    completeName = os.path.join(os.getcwd() + "/" + dirPath, fileName)
    f = open(completeName,"w")
    f.write(response)
    f.close()
    miniList = []
    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
        _link = link['href']
        #print "link " + _link
        if counter >= threshold or _link in urlIndices: break
        if _link not in urlIndices and _link not in tempurlDict:
            tempurlDict[_link] = True
            urlList3.append(_link)
            miniList.append(_link)
        if _link not in urlDict[curUrl]: urlDict[curUrl].append(_link)
        #print "list len " + str(len(urlList3)) +  " " + str(threshold)
        #print _link
    exit(miniList)

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
    print(urlIndices)
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
