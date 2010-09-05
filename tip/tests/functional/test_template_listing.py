#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import assert_equals

from tip import filters
from tip.actions import TemplatePathListingAction

action = TemplatePathListingAction()
template_paths = action.list_all_paths()
template_list = action.list_all_templates()

def test_listing_all_templates_on_valid_template_paths():
    i_have_3_template_paths()
    i_have_5_templates_on_those_template_paths()

def i_have_3_template_paths():
    assert_equals(len(template_paths), 3, 'should have 3 template paths')

def i_have_5_templates_on_those_template_paths():
    template_count = len(template_list)
    assert_equals(template_count, 5, 'should have 5 templates in valid paths')

def test_listing_invalid_templates_on_valid_template_paths():
    i_only_have_an_invalid_template()

def i_only_have_an_invalid_template():
    invalid_template_list = action.list_templates(filters.invalid)
    template_count = len(invalid_template_list)
    assert_equals(template_count, 1)
