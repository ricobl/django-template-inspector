#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import assert_equals

from tip.actions import TemplatePathListingAction

action = TemplatePathListingAction()
template_list = action.list_all_templates()

def test_listing_all_templates_on_valid_template_paths():
    i_have_3_template_paths()
    i_have_4_templates_on_those_template_paths()

def i_have_3_template_paths():
    assert_equals(len(template_list.keys()), 3, 'should have 3 template paths')

def i_have_4_templates_on_those_template_paths():

    template_count = sum(map(len, template_list.values()))
    assert_equals(template_count, 4, 'should have 4 templates in valid paths')
