#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import assert_equals
from os.path import join

from tip.tests.functional import current_dir
from tip.filesystem import FileSystem

folder_for_tests = join(current_dir,'files_for_testing')

def test_i_can_find_files_based_on_a_match():
    i_have_four_files_on_my_test_folder()
    i_have_five_files_when_supllying_a_global_matcher()
    i_have_five_file_when_no_matcher_is_provided()

def i_have_five_file_when_no_matcher_is_provided():
    found_files = FileSystem.locate(folder_for_tests)
    assert_equals(len(found_files), 5, 'exactly 5 files should"ve been found')

def i_have_four_files_on_my_test_folder():
    found_files = FileSystem.locate(folder_for_tests, '*.html')
    assert_equals(len(found_files), 4, 'exactly 4 files should"ve been found')

def i_have_five_files_when_supllying_a_global_matcher():
    found_files = FileSystem.locate(folder_for_tests, '*')
    assert_equals(len(found_files), 5, 'exactly 5 files should"ve been found')