import imp
import re
import json
import datetime

class QuoteSiteController:

    url = "https://meigen.keiziban-jp.com/"

    def __init__(self,driver):
        super().__init__()
        self.driver = driver
    
    def getTotalVisitors(self):
        self.driver.get(self.url)
        header = self.driver.find_element_by_id("header")
        text = header.find_element_by_class_name("acc").text
        totalVisitor = re.sub(r"\D", "", text)
        return totalVisitor
    
    def searchFor(self,keyword):
        self.driver.get(self.url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        textfield = self.driver.find_element_by_id("s")
        textfield.send_keys(keyword)
        searchButton = self.driver.find_element_by_id("searchsubmit")
        searchButton.click()

    def index0Open(self):
       postList =  self.driver.find_element_by_id("post_list")
       firstLi = postList.find_elements_by_tag_name("li")[0]
       aTag = firstLi.find_element_by_class_name("image")
       href = aTag.get_attribute("href")
       self.driver.get(href)
    
    
    def getPageQuotes(self):
        elements =  self.driver.find_elements_by_class_name("hreview")
        quoteList = []
        for element in elements:
            quote = self.__getQuote(element)
            quoteList.append(quote)
        dtNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        newFileName = "/app/src/data/quote{}.json".format(dtNow)
        print(newFileName)
        with open(newFileName, 'w') as f:
            json.dump(quoteList, f, ensure_ascii=False, indent=2)

    def __getQuote(self,element):
        quote = element.find_element_by_class_name("description").find_element_by_tag_name("p").text
        person = element.find_element_by_class_name("header").find_element_by_tag_name("h4").text
        data = {"quote": quote,"person": person}
        return data
       