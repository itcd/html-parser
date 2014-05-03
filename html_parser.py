# -*- coding: utf-8 -*-
"""
Created on Thu May 01 22:43:26 2014

@author: Shengzhou
"""

import time, urllib, sys, string
from HTMLParser import HTMLParser

ticker_list = ["socl", "ibb", "pnqi", "eirl", "ita", "iai", "xsd", "vbk", "dfe", "qqq", "ewi", "pbd"]
ticker = ""

class MyHTMLParser(HTMLParser):
    previous_data = ""
    text_before_amp = ""

    def handle_starttag(self, tag, attrs):
        # get arrow diection: up/positive or down/negative
        for attr in attrs:
            if "down_r time_rtq_content"==attr[1]:
                sys.stdout.write("\t-")
            if "up_g time_rtq_content"==attr[1]:
                sys.stdout.write("\t+")

    def handle_data(self, data):
        starttag_text = self.get_starttag_text()

        # get stock/fund name
        if -1!=string.find(data, ("(%s)" % ticker).upper()) and -1!=string.find(starttag_text, "<h2>"):
            if ""!=self.text_before_amp:
                sys.stdout.write(self.text_before_amp + "&")
            sys.stdout.write(data)

        # get percentage changed
        if -1!=string.find(str(starttag_text), "yfs_p43_%s" % ticker.lower()) and -1!=string.find(data, "("):
            sys.stdout.write(data.replace("(", "").replace(")", ""))

        # get date of quotes
        if -1!=string.find(str(starttag_text), "yfs_t53_%s" % ticker.lower()):
            t = time.strptime(data.split(",")[0] + time.strftime(" %Y"), "%b %d %Y")
            sys.stdout.write("\t" + time.strftime("%d/%m/%Y", t))

        # get the day's range - lower value
        if -1!=string.find(str(starttag_text), "yfs_g53_%s" % ticker.lower()) and -1==string.find(data, "-"):
            sys.stdout.write("\t" + data)

        # get the day's range - upper value
        if -1!=string.find(str(starttag_text), "yfs_h53_%s" % ticker.lower()):
            print "\t", data

        self.previous_data = data

    def handle_entityref(self, name):
        # for stock names with the symbol &, save the part before & for later use
        if "amp"==name and -1!=string.find(self.get_starttag_text(), "<h2>"):
            self.text_before_amp = self.previous_data

for t in ticker_list:
    ticker = t
    parser = MyHTMLParser()
    f = urllib.urlopen("http://finance.yahoo.com/q?s=%s" % ticker)
    html_string = f.read()
    parser.feed(html_string)
