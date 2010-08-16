#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

from django.conf import settings
from nose.tools import assert_equals

from tip.tests.helpers import abs, LoggableDevice
from tip.management.commands import tip

command = tip.Command()

def test_i_have_a_template_path_listing_command():
    i_have_a_command_to_list_all_template_path()
    invoking_the_listing_command_returns_all_paths()
    
def i_have_a_command_to_list_all_template_path():

    command.handle(show_templates_path=True)

    assert_equals(command.show_templates_path, 
                    True, 
                    'should enable template path listing %s' % command.show_templates_path)

def invoking_the_listing_command_returns_all_paths():

    command.handle(show_templates_path=True)

    assert abs(settings.ROOT_DIR, 'templates') in sys.stdout.outputs, 'Should return a list of paths'

original_stdout = sys.stdout
def setUp():
    sys.stdout = LoggableDevice()

def tearDown():
    sys.stdout = original_stdout

