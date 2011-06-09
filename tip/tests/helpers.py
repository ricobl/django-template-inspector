#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

def abs(*paths):
    return os.path.abspath(os.path.join(*paths))

class LoggableDevice(object):
    outputs = None

    def __init__(self):
        self.outputs = []

    def write(self, s):
        self.outputs.append(s)

    def isatty(self):
        return False
