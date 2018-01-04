from Pagerank import pageRank
from TFIDF import indexer
from multiprocessing import Process
import json
import ast

def Combine(num_processes):
	invIndFile = open('invindex.txt', 'w')
	docsFile = open('docs.txt', 'w')
	finalDocsDict = {}
	finalInvDict = {}
	for i in range(1, num_processes + 1):
		with open('docs' + str(i) + '.txt', 'r') as curDFile:
			curDDict = ast.literal_eval(curDFile.read())
		finalDocsDict.update(curDDict)

		curIFile = open('invindex' + str(i) + '.txt')
		curIDict = json.load(curIFile)
		for key in curIDict:
			if key not in finalInvDict:
				finalInvDict[key] = curIDict[key]
			else:
				finalInvDict[key].update(curIDict[key])
	invIndFile.write(json.dumps(finalInvDict))
	invIndFile.close()

	docsFile.write(json.dumps(finalDocsDict))
	docsFile.close()



def splitIndex(Num_Of_Processors):
	indextxt = open("index.txt",'r')
	lines = indextxt.readlines()
	num_of_links = len(lines)
	extra = num_of_links % Num_Of_Processors
	num_of_links = num_of_links - extra
	links_per_Processor = num_of_links/Num_Of_Processors

	index = 0
	for i in range(1,5):
		if i == 4:
			links_per_Processor = links_per_Processor + extra
		with open('index' + str(i) + ".txt", 'w') as file:
			for j in range(index, index + links_per_Processor):
				file.write(lines[j])
				index = index + 1


if __name__ == "__main__":
	pageRank()
	splitIndex(4)
	processes = []
	numProcesses = 4
	for i in range(1, numProcesses + 1):
		p = Process(target=indexer, args=('CrawledPages','index' + str(i) + '.txt', i))
		p.start()
		processes.append(p)

	for p in processes:
		p.join()

	Combine(len(processes))
	# indexer("CrawledPages", "index.txt")
