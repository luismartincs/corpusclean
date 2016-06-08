#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs

class CorpusUtils:

   def __init__(self):
      print "Start"
   
   def cleanCorpus(self):
      f = codecs.open('data.txt', 'r','UTF-8')
      content = f.read().replace('\n', '')
      print content

cu = CorpusUtils()
cu.cleanCorpus()