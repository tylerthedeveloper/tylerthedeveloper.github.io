import json
import nltk
from nltk.corpus import stopwords
import collections
import string
import nltk.stem.porter as p
import collections
import string
import nltk.stem.porter as p
import math
from decimal import Decimal, getcontext
from operator import itemgetter

import math
from decimal import Decimal, getcontext
from operator import itemgetter


''' ------------------  PART 1 ------------------  '''

# Global Indexes
docIndex = {}
invIndex = {}
pageRankScores = {}

with open('docs.txt','r') as inf:
    docIndex = eval(inf.read())

with open('invindex.txt','r') as inf:
    invIndex = eval(inf.read())

with open('pagerank_scores.txt','r') as inf:
    pageRankScores = eval(inf.read())

#score function
def calcTFIDFscore(curSum, fullSum, foundDocs):
    allDocs = len(docIndex.keys())
    #print str(curSum) + " "  + str(fullSum) + " " + str(foundDocs)
    getcontext().prec = 10
    tf = Decimal(curSum) / Decimal(fullSum)
    #idf = math.log(allDocs / (1 + foundDocs))
#    idf = Decimal(1) / Decimal(1 + math.log(foundDocs))
    idf = Decimal(1) / Decimal(1 + math.log(foundDocs))
    #print str(tf) + " " + str(idf)
    return tf * idf


def retrieval(mode, searchWords):
    stemmedSearch = []
    stemmer = p.PorterStemmer()
    stops = open("stopwords.txt", "r")
    count = 0

    for word in searchWords:
        if word not in stops:
            stemmedSearch.append(stemmer.stem(word))


    if mode == "or":
        tempDict = {}
        tupleList = []
        calcList = []
        for word in stemmedSearch:
            #print word
            word = word.lower()
            if word not in invIndex: continue
            docs = invIndex[word].keys()
            docListLength = len(docs)
            for doc in docs:
                if doc not in tempDict.keys():
                    tempDict[doc] = True
                    score = calcTFIDFscore(invIndex[word][doc], docIndex[doc]['Document_Length'], docListLength)
                    link = docIndex[doc]['Link']
                    score *= Decimal(pageRankScores[link])
                    title = docIndex[doc]['Document_Title']
                    calcList.append(Decimal(score))
                    tupleList.append((score, link, title))
                count = count + 1
        tupleList = sorted(tupleList, reverse=True)
        calcList.sort(reverse=True)
        count25 = 0
#         for cal in calcList:
#             for doc in tempDict:
#                 if (count25 < 25) and (cal == tempDict[doc]['TFIDF']):
#                     # print (str(count25))
# #                    tempDict[doc]['index'] = count25
#                     count25 = count25 + 1
        return tupleList if len(tupleList) < 25 else tupleList[0:25]

# print(retrieval("or", ["States", "United"]))

