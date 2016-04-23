#!/usr/bin/python

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import os.path

class myCounterHandler(ContentHandler):
    if os.path.exists("bp.html"):
        fichHTML = open("bp.html", "w")
    else:
        fichHTML = open("bp.html", "a")
    title = ""
    link = ""

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
    #    self.response = ""
    def startElement (self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True

    def endElement (self, name):
        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                self.title = self.theContent.encode('utf-8')
                print self.title
                #line = "Title : " + self.theContent + "."
                #self.title = normalize_whitespace(self.theContent)
                self.inContent = False
                self.theContent = ""
                #print line.encode('utf-8')
            elif name == 'link':
                self.link = self.theContent.encode('utf-8')
                print self.link
                line = "<li><a href =" + self.link + ">"+ self.title +"</a></li></br>"
                self.fichHTML.write(line)
                self.inContent = False
                self.theContent = ""


    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars

# --- Main prog

if len(sys.argv)<2:
    print "Usage: python parse.py <document>"
    print " <document>: file name of the document to parse"
    sys.exit(1)

# Load parser and driver

Parser = make_parser()
Handler = myCounterHandler()
Parser.setContentHandler(Handler)
print "Good job, parse complete ! "
# Ready, set, go!

xmlFile = open(sys.argv[1],"r")
Parser.parse(xmlFile)

print "Parse complete"

#File = open("barra_punto.html","w")
#File.write(Handler.response.encode('utf8'))
#print Handler.response
