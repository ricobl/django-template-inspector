#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

from django.conf import settings
from nose.tools import with_setup

from tip.tests.helpers import abs, LoggableDevice
from tip.management.commands import tip

command = tip.Command()

original_stdout = sys.stdout
def setup_stdout():
    sys.stdout = LoggableDevice()

def teardown_stdout():
    sys.stdout = original_stdout

@with_setup(setup_stdout, teardown_stdout)
def test_i_have_a_template_path_listing_command():
    i_have_a_sub_command_to_list_all_template_path()
    invoking_the_listing_command_returns_all_paths()
    
def i_have_a_sub_command_to_list_all_template_path():
    assert 'dirs' in command.sub_commands,\
            'should enable template path listing %s' % command.show_templates_path

def invoking_the_listing_command_returns_all_paths():
    command.handle('dirs')
    expected = abs(settings.ROOT_DIR, 'templates')
    assert expected in sys.stdout.outputs,\
            'Should return a list of paths'

