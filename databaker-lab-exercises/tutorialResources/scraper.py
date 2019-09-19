import os

from IPython.display import display, Markdown
from databaker.framework import loadxlstabs

# Stringifys some metadata-like output for the fake scrape
def fakeMetadata(metaDict):
    firstEntry = True
    for k, v in metaDict.items():
        if firstEntry:
            display(Markdown('**{}**\n'.format(k)))
            display(Markdown('{}\n'.format(v)))
            firstEntry = False
        else:
            display(Markdown('**{}**\n'.format(k)))
            display(Markdown('{}\n'.format(v)))
    return ""

class Scraper(object):
    
    def __init__(self, url):
        
        self.metaData = {}
        self.distribution = fakeDistribution()
        self.location = os.path.dirname(os.path.abspath(__file__)) + "/spreadsheets/"

        if url == "https://www.fake-website.com/example1":
            self.metaData.update({"Example dataset 1": "this is an example dataset for the walkthroughs."})
            
            try:
                self.distribution.tabs = loadxlstabs(self.location + "databakerExample1.xlsx", verbose=False)
            except:
                raise ValueError("Can't open", self.location + "databakerExample1.xlsx")
            
    def __repr__(self):
        return fakeMetadata(self.metaData)
        
            
class fakeDistribution(object):
    
    def __init__(self):
        self.tabs = None
        
    def as_databaker(self):
        return self.tabs
        