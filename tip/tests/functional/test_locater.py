#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import assert_equals
from os.path import join

from tip.tests.functional import current_dir
from tip.filesystem import FileSystem

def test_i_can_find_files_based_on_a_match():
    i_have_four_files_on_my_test_folder()

def i_have_four_files_on_my_test_folder():
    found_files = FileSystem.locate(join(current_dir,'files_for_testing'), '*.html')
    assert_equals(len(found_files), 4, 'exactly 4 files should"ve been found')