#!/usr/bin/env python
#-*- coding:utf-8 -*-

import fnmatch

import os
from os.path import abspath, join, dirname, curdir, exists

class FileSystem(object):
 
    @classmethod
    def locate(cls, path, match=None):
        root_path = abspath(path)
        return_files = []
        for path, dirs, files in os.walk(root_path):
            for filename in files:
                if match:
                    if fnmatch.fnmatch(filename, match):
                        return_files.append(join(path, filename))
                    continue

                return_files.append(join(path, filename))

        return return_files
