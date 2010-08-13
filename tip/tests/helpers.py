#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

def abs(*paths):
    return os.path.abspath(os.path.join(*paths))
