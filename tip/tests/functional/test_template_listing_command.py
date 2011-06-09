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
def test_i_have_a_template_listing_command():
    i_have_a_sub_command_to_list_all_templates()
    invoking_the_listing_command_returns_all_templates()
    i_have_an_invalid_template()

def i_have_a_sub_command_to_list_all_templates():
    assert 'list' in command.sub_commands

def invoking_the_listing_command_returns_all_templates():
    command.handle('list')
    expected = abs(settings.ROOT_DIR, 'dummy_app1/templates/base_app1.html')
    assert expected in sys.stdout.outputs, '"%s" expected in "%s"' \
            % (expected, sys.stdout.outputs)

def i_have_an_invalid_template():
    command.handle('list')
    expected = abs(settings.ROOT_DIR, 'dummy_app1/templates/invalid_template.html')
    assert expected in sys.stdout.outputs, 'should have an invalid template'

@with_setup(setup_stdout, teardown_stdout)
def test_i_have_an_invalid_template_listing_command():
    i_have_a_sub_command_to_list_invalid_templates()
    invoking_the_listing_command_returns_only_invalid_templates()

def i_have_a_sub_command_to_list_invalid_templates():
    assert 'invalid' in command.sub_commands

def invoking_the_listing_command_returns_only_invalid_templates():
    command.handle('invalid')
    expected = abs(settings.ROOT_DIR, 'dummy_app1/templates/invalid_template.html')

    not_expected = abs(settings.ROOT_DIR, 'dummy_app1/templates/base_app1.html')

    assert expected in sys.stdout.outputs, 'should have an invalid template'
    assert not_expected not in sys.stdout.outputs, "shouldn't list valid templates"

