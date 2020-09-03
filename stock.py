from selenium import webdriver
from bs4 import BeautifulSoup
import json
import requests
from progress.bar import Bar
class Bourse:
    def __init__(self, *args, **kwargs):
          
        my_url = "http://www.tsetmc.com/Loader.aspx?ParTree=15131F"
        print("start conecting")
        driver = webdriver.PhantomJS()
        driver.get(my_url)
        html = driver.page_source
        driver.quit()
        self.htmlParserObject = BeautifulSoup(html,"html.parser")
        #get symbols href
        self.get_symbols_href=["http://www.tsetmc.com/"+item["href"] for item in self.htmlParserObject.findAll('a',{'class' : 'inst'}, limit=None)]  
    #Get groups in Dict Form   
    def get_symbols_groups(self):
        findClass = self.htmlParserObject.findAll('div',{'class' : 'secSep'}, limit=None)
        groups = {item['id'] : item.text for item in findClass}
        return groups
    

    def get_symbol_info(self):
        findDiv= self.htmlParserObject.findAll('div',limit=None)
        findLinks = self.htmlParserObject.findAll('a',{'class':'inst'},limit=None)
        dictOfLinks={}
        findLinkBar= Bar("link adding",max=len(findLinks))
        for item in findLinks:
            if item['target'] in dictOfLinks.keys():
                listSelect=dictOfLinks[item['target']]
                listSelect.append(item.text)
                findLinkBar.next()
            else:
                 dictOfLinks[item['target']]=[item.text]
                 findLinkBar.next()
                  
        symbolInfo = []
        group=None
        bar = Bar('div extacter', max=len(findDiv))
        for div in findDiv:
            divattrs= [key for key in (div.attrs).keys()]
            if 'class' in divattrs:
                if div.attrs["class"] == ["secSep"]: 
                    group=div['id']
                if div.attrs["class"] == ["{c}"] and group is not None:
                    name_namad_List=dictOfLinks[div['id']]
                    symbolInfo.append({'name':name_namad_List[1],
                                    'id':div['id'],
                                    'namad':name_namad_List[0],
                                    'group':group})
                elif div.attrs["class"] == ["{c}"] and group is None:
                    raise "group can not be null,"+{'name':name_namad_List[1],
                                    'id':div['id'],
                                    'namad':name_namad_List[0],
                                    'group':group}        
            bar.next()

        return symbolInfo    
    

class SymbolsTse:
    def get_all_symbols(self):
        response = requests.get("http://www.tsetmc.com/Loader.aspx?ParTree=111C1417")
        bso= BeautifulSoup(response.text,"html.parser")
        findLinks = bso.findAll('a',{'class':'','id':'','target':'_blank'},limit=None)
        all_symbols_list = [item.text for item in findLinks]
        return all_symbols_list

    
    