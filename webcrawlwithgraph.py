def add_to_index(index, keyword, url):  ##chaged from list to dict
	if keyword in index:
		index[keyword].append(url)
	else:
		index[keyword] = [url]
"""
	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
	index.append([keyword, [url]])
"""

def add_page_to_index(index, url, content): #content contains all the keyword
	words = content.split()
	for word in words:
		add_to_index(index, word, url)

def lookup(index, keyword):

	if keyword in index:
		return index[keyword]
	else:
		return None

"""
	for entry in index:
		if entry[0] == keyword:
			return entry[1]
	return None
"""

"""index = []
add_page_to_index(index, 'http://dilbert.com', "hello word good moring")
print index"""

def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index = {}
	graph = {}
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index, page, content)
			outlinks = get_all_links(content)
			graph[page] = outlinks
			union(tocrawl, outlinks)
			crawled.append(page)
	return index, graph

def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ""

def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

def compute_ranks(graph):
	d = 0.8
	numloops = 10

	ranks = {}
	npages = len(graph)
	for page in graph:
		ranks[page] = 1.0 / npages
	
	for i in range(0, numloops):
		newranks = {}
		for page in graph:
			newrank = (1 - d) / npages
			for node in graph:
				if page in graph[node]:	
					newrank = newrank + d * (ranks[node] / len(graph[node]))
			newranks[page] = newrank
		ranks = newranks
	return ranks











