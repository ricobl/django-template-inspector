#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

from django.conf import settings
from nose.tools import assert_equals

from tip.tests.helpers import abs, LoggableDevice
from tip.management.commands import tip

command = tip.Command()

def test_i_have_a_template_listing_command():
    i_have_a_command_to_list_all_templates()
    invoking_the_listing_command_returns_all_templates()

def i_have_a_command_to_list_all_templates():

    command.handle(list_templates=True)

    assert_equals(command.list_templates, 
                    True, 
                    'should enable template listing %s' % command.list_templates)

def invoking_the_listing_command_returns_all_templates():
    command.handle(list_templates=True)

    assert "\t\033[32m%s\033[0m" % abs(settings.ROOT_DIR, 'dummy_app1/templates/base_app1.html') in sys.stdout.outputs, 'return a list of templates'

original_stdout = sys.stdout
def setUp():
    sys.stdout = LoggableDevice()

def tearDown():
    sys.stdout = original_stdout
