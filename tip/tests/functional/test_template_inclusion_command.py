#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys

from django.conf import settings
from nose.tools import assert_equals, with_setup

from tip.tests.helpers import abs, LoggableDevice
from tip.management.commands import tip


command = tip.Command()

original_stdout = sys.stdout
def setup_stdout():
    sys.stdout = LoggableDevice()

def teardown_stdout():
    sys.stdout = original_stdout

@with_setup(setup_stdout, teardown_stdout)
def test_i_have_a_template_inclusion_command():
    i_have_a_sub_command_to_list_all_templates()
    invoking_the_listing_command_returns_all_templates()

def i_have_a_sub_command_to_list_all_templates():
    assert 'includes' in command.sub_commands

def invoking_the_listing_command_returns_all_templates():
    command.handle('includes', 'base_app1.html')

    expected = os.path.join(settings.ROOT_DIR,
                            'dummy_app1/templates/included_content/my_content.html')

    assert expected in sys.stdout.outputs, 'Base template for inclusion expected'
