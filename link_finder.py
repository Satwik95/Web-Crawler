from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class LinkFinder(HTMLParser):

	#def _init_(self):
	#	super().__init__()

    def handle_starttag(self, tag, attrs):
    	if tag == 'a':
    		for (attribute,value) in attrs:
    			if attribute == 'href':
    				url = parse.urljoin(self.base_url,value)
    				self.links.add(url)
        print(tag)

    def error(self,message):
    	pass

    def __init__(self,base_url,page_url):
    	HTMLParser.__init__(self)
    	self.base_url = base_url
    	self.page_url = page_url
    	self.links = set()

    def page_links(self):
    	return self.links

# instantiate    the parser and fed it some HTML
#finder = LinkFinder()
#finder.feed('<html><head><title>Test</title></head>'
 #           '<body><h1>Parse me!</h1></body></html>')