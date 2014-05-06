# -*- coding: utf-8 -*-
"""
Created on Thu May 01 22:43:26 2014

@author: Shengzhou
"""

import time, urllib, sys
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    previous_data = ""
    text_before_amp = ""
    negative = False

    def __init__(self, t):
        HTMLParser.__init__(self)
        self.ticker = t

    def handle_starttag(self, tag, attrs):
        # get arrow diection: up/positive or down/negative
        for attr in attrs:
            if "up_g time_rtq_content"==attr[1]:
                self.negative = False
            if "down_r time_rtq_content"==attr[1]:
                self.negative = True

    def handle_data(self, data):
        starttag_text = self.get_starttag_text()
        
        # get market time and print its date
        # pre market string "Tue, May 6, 2014, 9:02AM EDT - US Markets open in 28 mins" "Tue, May 6, 2014, 8:57AM EDT - U.S. Markets open in 33 mins."
        # in market string "Mon, May 5, 2014, 10:50AM EDT - US Markets close in 5 hrs and 10 mins"
        # after market string "Mon, May 5, 2014, 5:41pm EDT - US Markets are closed"
        if -1 != str(starttag_text).find("yfs_market_time") and -1 != data.find(","):
            s = data.split(",")
            t = time.strptime(s[0] + s[1] + s[2], "%a %b %d %Y")
            sys.stdout.write(time.strftime("%d/%m/%Y", t))

        # get stock/fund name
        if -1 != data.find(("(%s)" % self.ticker).upper()) and -1 != str(starttag_text).find("<h2>"):
            sys.stdout.write("\t" + self.ticker + "\t")
            if len(self.text_before_amp.strip()) > 0:
                sys.stdout.write(self.text_before_amp + "&")
            sys.stdout.write(data)

        # get quote
        if -1 != str(starttag_text).find("yfs_l84_%s" % self.ticker.lower()) and len(data.strip()) > 0:
            sys.stdout.write("\t" + data)
            
        # get percentage change. the tag id is "yfs_p43_%s" in or after trading hours, or "yfs_p20_%s" pre-market.
        if (-1 != str(starttag_text).find("yfs_p43_%s" % self.ticker.lower()) or -1 != str(starttag_text).find("yfs_p20_%s" % self.ticker.lower())) and len(data.strip()) > 0:
            sys.stdout.write("\t")
            if self.negative:
                sys.stdout.write("-")
            sys.stdout.write(data.strip("()"))

        # get date of quote if it exists. the date only appears before market open.
        # pre market string "May 5, 4:00PM EDT"
        # in market string "10:50AM EDT"
        # after market string "4:00PM EDT"
        if -1 != str(starttag_text).find("yfs_t53_%s" % self.ticker.lower()) and -1 != data.find(","):
            t = time.strptime(data.split(",")[0] + time.strftime(" %Y"), "%b %d %Y")
            sys.stdout.write("\t" + time.strftime("%d/%m/%Y", t))

        # get the day's range - lower value
        if -1 != str(starttag_text).find("yfs_g53_%s" % self.ticker.lower()) and len(data.strip(" -")) > 0:
            sys.stdout.write("\t" + data)

        # get the day's range - upper value
        if -1 != str(starttag_text).find("yfs_h53_%s" % self.ticker.lower()):
            sys.stdout.write("\t" + data)

        self.previous_data = data

    def handle_entityref(self, name):
        # for stock names with the symbol &, save the part before & for later use
        if "amp" == name and -1 != str(self.get_starttag_text()).find("<h2>"):
            self.text_before_amp = self.previous_data

if __name__ == "__main__":
    # default values
    ticker_list = ["ibb", "ita", "qqq", "xsd"]

    # arguments can be passed through command line.
    # usage: python parser.py "ibb ita qqq xsd" > output.txt
    if len(sys.argv) > 1:
        ticker_list = sys.argv[1].split()

    for t in ticker_list:
        parser = MyHTMLParser(t)
        filehandle = urllib.urlopen("http://finance.yahoo.com/q?s=%s" % t)
        html_string = filehandle.read()
        parser.feed(html_string)
        parser.close()
        print
