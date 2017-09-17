from lxml import html
import requests

class Spider():
    def __init__(self, url):
        self._url = url;
        self._page = requests.get(self._url);
        self._tree = html.fromstring(self._page.content)
        self._info = [];
        
    #parses the path obj
    #strips each string in the list and filters list
    def parse(self, path):
        self._delete_info();
        self._info = self._tree.xpath(path);
        self._info = list(map(str.strip, self._info))
        self._info = list(filter(None, self._info));

    #returns list of information
    def get_info(self):
        return self._info
    
    #clears the list
    def _delete_info(self):
        self._info = list();
        
    #displays information
    def display_info(self):
        print(self._info);
