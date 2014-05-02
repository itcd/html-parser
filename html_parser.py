# -*- coding: utf-8 -*-
"""
Created on Thu May 01 22:43:26 2014

@author: Shengzhou
"""

import time
import urllib
import sys
import string
from HTMLParser import HTMLParser

ticker_list = ["socl", "ibb", "pnqi", "eirl", "ita", "iai", "xsd", "vbk", "dfe", "qqq", "ewi", "pbd"]
ticker = ""

class MyHTMLParser(HTMLParser):
    previous_data = ""
    text_before_amp = ""
    
    def handle_data(self, data):
        starttag_text = self.get_starttag_text()
        
        if -1!=string.find(data, ("(%s)" % ticker).upper()) and -1!=string.find(starttag_text, "<h2>"):
            sys.stdout.write(time.strftime("%d/%m/%Y") + "\t")
            if ""!=self.text_before_amp:
                sys.stdout.write(self.text_before_amp + "&")
            sys.stdout.write(data)
            
        if -1!=string.find(str(starttag_text), "yfs_g53_%s" % ticker.lower()) and -1==string.find(data, "-"):
            sys.stdout.write("\t" + data)
            
        if -1!=string.find(str(starttag_text), "yfs_h53_%s" % ticker.lower()):
            print "\t", data
            
        self.previous_data = data
            
    def handle_entityref(self, name):
        if "amp"==name and -1!=string.find(self.get_starttag_text(), "<h2>"):
            self.text_before_amp = self.previous_data

for t in ticker_list:
    ticker = t
    parser = MyHTMLParser()
    f = urllib.urlopen("http://finance.yahoo.com/q?s=%s" % ticker)
    html_string = f.read()
    parser.feed(html_string)
