# -*- coding: utf-8 -*-
"""
Created on Thu May 01 22:43:26 2014

@author: Shengzhou
"""

import urllib
import sys
import string
from HTMLParser import HTMLParser

ticker_list = ["ibb", "socl", "pnqi", "qqq", "vbk", "eirl", "ewi", "pbd", "ita", "dfe"]
ticker = ticker_list[0]

class MyHTMLParser(HTMLParser):      
    def handle_data(self, data):
        starttag_text = self.get_starttag_text()

        ticker_str = "(%s)" % ticker
        if -1!=string.find(data, ticker_str.upper()) and -1!=string.find(starttag_text, "<h2>"):
            sys.stdout.write(data)
            
        if -1!=string.find(str(starttag_text), "yfs_g53_%s" % ticker.lower()) and -1==string.find(data, "-"):
            sys.stdout.write("\t")
            sys.stdout.write(data)
            
        if -1!=string.find(str(starttag_text), "yfs_h53_%s" % ticker.lower()):
            print "\t", data

for t in ticker_list:
    ticker = t
    parser = MyHTMLParser()
    f = urllib.urlopen("http://finance.yahoo.com/q?s=%s" % ticker)
    html_string = f.read()
    parser.feed(html_string)
