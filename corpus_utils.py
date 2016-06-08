#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import re
import csv

class CorpusUtils:

   punctuation = "['.?!:;/\"\'\-()\[\],\\\]"
   conectors = ["i","you","he","she","they","that","are","to","of","at","given","also","can","be","not","either",
               "does","take","have","the","an","do","as","it","a","dont","or","b","ive","which","if","youll","with",
               "want","in","is","so","your","for","where","our","this","its","we","re","’","and","has","would","don"
               "isnt","will","how","much","youd","whatever","since","may","called","thats"]
   content = ""
   global_headers = []
   word_list = {}

   input_file = ""
   output_file = ""

   def __init__(self):
      self.loadHeaders()
   

   def loadHeaders(self):
      f = codecs.open('headers.txt', 'r','UTF-8')
      for line in f:
         self.global_headers.append(line.replace('\n', ''))
      print "Cargando encabezados"


   def generateIMCSV(self,filesarr):

      writer = csv.writer(open("IM.csv", 'wb'))

      headers_row = list(self.global_headers)
      headers_row.insert(0,"Document")
      writer.writerow(headers_row)

      i = 0
      while(i < len(inputs)):
         new_row = []
         new_row.append(filesarr[i])

         self.readCSVToDictionary(filesarr[i])
         #print "ROW\n\n"
         for header in self.global_headers:
            if header not in self.word_list:
               #print "se agrega con incidencia 0"
               self.word_list[header] = 0

            new_row.append(self.word_list[header])
            #print ("%s:%s" % (header,self.word_list[header]))
         writer.writerow(new_row)
         i = i+1

   def analyze(self,inputf,outputf):
      self.input_file = inputf
      self.output_file = outputf

      f = codecs.open(self.input_file, 'r','UTF-8')

      self.word_list = {}
      self.content = f.read().replace('\n', '')
      self.removePunctiation()
      self.removeWords()
      self.createList()
      self.showList()
      self.writeListToCSV()
      self.writeHeaders()

   def removePunctiation(self):
      self.content = re.sub(self.punctuation, '', self.content)

   def removeWords(self):
      remove = '|'.join(self.conectors)
      regex = re.compile(r'\b('+remove+r'|\w|\w\w)\b', flags=re.IGNORECASE)
      self.content = regex.sub("", self.content)

   def createList(self):
      for word in (' '.join(self.content.split())).split(" "):
         lword = word.lower()

         if lword in self.word_list:
            self.word_list[lword] = self.word_list[lword]+1
         else:
            self.word_list[lword] = 1

   def showList(self):
      print self.word_list

   def writeHeaders(self):
      writer = open('headers.txt', 'wb')
      for key in self.word_list:
         if key not in self.global_headers:
            self.global_headers.append(key)
         else:
           print "Si esta el header %s" % key

      for word in self.global_headers:
         writer.write(word+"\n")

   def writeListToCSV(self):
      writer = csv.writer(open(self.output_file, 'wb'))
      for key, value in self.word_list.items():
         writer.writerow([key, value])

   def readCSVToDictionary(self,filename):
      reader = csv.reader(open(filename, 'rb'))
      self.word_list = dict(reader)


cu = CorpusUtils()
inputs = ["data1.txt","data2.txt","data3.txt"]
outputs = ["c1.csv","c2.csv","c3.csv"]
'''
i = 0

while(i < len(inputs)):
   cu.analyze(inputs[i],outputs[i])
   i = i+1
'''
cu.generateIMCSV(outputs)

