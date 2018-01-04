import json
#import nltk
##nltk.download()
import nltk
# nltk.download('punkt')
import urllib2
from nltk.corpus import stopwords
import collections
import string
import nltk.stem.porter as p
import collections
import string
import nltk.stem.porter as p
from bs4 import BeautifulSoup
from bs4.element import Comment



# Global Indexes
invIndex = {}
docIndex = {}

# Helper function for getting relevant text
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

#Create a stemmed list of words given certain document
def createWordList(file, dirname):
  url = str(dirname + "/" + file)
  page = open(url)
  soup = BeautifulSoup(page.read(), from_encoding = 'utf-8')
  texts = soup.findAll(text = True)
  visible_text = filter(tag_visible,texts)
  vs = []
  words = []
  exclude = set(string.punctuation)
  for w in visible_text:
    word = w.replace("\t", "").replace("\n", "").strip()
    word = ''.join(ch for ch in word if ch not in exclude)
    vs.append(word.lower())
  for w in vs:
    line = w.split(" ")
    if (len(line) > 1):
      for _w in line:
        words.append(_w)
  return words

#Creates Inverted index
def parser(wordList, file):
  nltk.word_tokenize(str(wordList))
  stops = open("stopwords.txt", "r")
  noStops = []
  for word in wordList:
    if word not in stops:
      noStops.append(word)
  stemmer = p.PorterStemmer()
  stems = [stemmer.stem(word) for word in noStops]
  for word in stems:
        if word not in invIndex:
            invIndex[word] = {}
        if file not in invIndex[word]:
            invIndex[word][file] = 1
        else:
            curCount = invIndex[word][file]
            invIndex[word].update({file : curCount + 1})

#creates docs.txt
def docIndexer(wordList, file, url):
    try:
        soup = BeautifulSoup(urllib2.urlopen(url))
        docTitle = soup.title.string
        docLength = len(wordList)
        docIndex[file] = {}
        docIndex[file].update({"Link": url})
        docIndex[file].update({"Document_Title": docTitle})
        docIndex[file].update({"Document_Length": docLength})
    except:
        docTitle = url
        docLength = len(wordList)
        docIndex[file] = {}
        docIndex[file].update({"Link": url})
        docIndex[file].update({"Document_Title": docTitle})
        docIndex[file].update({"Document_Length": docLength})


#Brings everything together to construct both output files
def indexer(dirname, fileMapper, ID):
    wordList = []
    _fileMap = open(fileMapper, "r")
    for lines in _fileMap:
        line = lines.split()
        file = line[0]
        url = line[1]
        wordList = createWordList(file, dirname)
        parser(wordList, str(file))
        docIndexer(wordList, file, url)

    with open("invindex" + str(ID) + ".txt", "w") as file:
      file.write(json.dumps(invIndex))
      file.close()

    with open('docs'  + str(ID) + '.txt', 'w') as file:
      file.write(json.dumps(docIndex))
      file.close()
