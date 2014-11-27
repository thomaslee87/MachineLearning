#!/usr/bin/env python
import os

class Dataset(object):
    """docstring for Dataset"""
    def __init__(self, arg):
        self.__feature = []
        self.__data = []

    def load_data(self, file):
        if not os.path.isfile(file):
            return False
        fd = open(file, 'r')
        

        fd.close()
