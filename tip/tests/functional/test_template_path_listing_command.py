#!/usr/bin/env python
#-*- coding:utf-8 -*-

from tip.management.commands import tip
from nose.tools import assert_equals, assert_not_equals

def test_i_have_a_template_path_listing_comma():
    """testing if i have a command to list all template paths"""
    i_have_a_command_to_list_all_template_path()
    
def i_have_a_command_to_list_all_template_path():
    command = tip.Command()

    command.handle(show_templates_path=True)

    assert_equals(command.show_templates_path, 
                    True, 
                    'should enable template listing %s' % command.show_templates_path)
