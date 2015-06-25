from html.parser import HTMLParser # to extract all text from the HTML code of the page
from urllib.request import urlopen # opens communiaction link with a URL
from urllib import parser # 

class LinkParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for (key, value) in attrs:
				if key == "href":
					newURL = parse.urljoin(self.baseurl, value)
					self.links = self.links + [newURL]

	def getLinks(self, url):
		self.links = []
		self.baseurl = url
		response = urlopen(url)
		if response.getheader9('Content-Type') == "text/html":
			htmlBytes = response.read()
			htmlString = htmlBytes.decode("utf-8")
			self.feed(htmlString)
			return htmlString, self.links
		else:
			return "", []

	def spider(url, word, maxPages):
		pagesToVisit = [url]
		numberVisited = 0
		foundWord = False
		while numberVisited < maxPages and pagesToVisit != [] and not foundWord:
			numberVisited = numberVisited + 1
			url = pagesToVisit[0]
			pagesToVisit = pagesToVisit[1:]
			try:
				print (numberVisited, "Visiting: ", url)
				parser = LinkParser()
				data, links = parser.getLinks(url)
				if data.find(word) > -1:
					foundWord = True
				pagesToVisit = pagesToVisit + links
				print('Success!!')
			except:
				print("Failed!!")



