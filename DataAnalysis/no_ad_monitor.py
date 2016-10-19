# !/usr/bin/env python
# -*-coding:utf-8-*-

import csv

class AdMonitor(object):

    __FileName = None

    def __init__(self,filename):
        self.__FileName = filename

    def run(self):
        try:
            csvFile = file(self.__FileName,'rb')
            lines = csv.reader(csvFile)
            for line in lines:
                print line
                break
            csvFile.close()
        except Exception , ex:
            raise ex