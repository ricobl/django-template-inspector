#!/usr/bin/env python
#-*- coding:utf-8 -*-

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


def test_i_have_a_help_sub_command():
    assert 'help' in command.sub_commands

@with_setup(setup_stdout, teardown_stdout)
def test_invoking_help_without_params_shows_help():
    command.handle('help')
    content = ''.join(sys.stdout.outputs)
    assert content

@with_setup(setup_stdout, teardown_stdout)
def test_default_help_shows_available_sub_commands():
    from tip.management.commands.tip import ShowHelp
    command.handle('help')
    output = ''.join(sys.stdout.outputs)
    assert 'Available sub-commands:' in output
    assert '  help                  %s' % ShowHelp.help.strip() in output, ShowHelp.help + '\n\n\n\n' + output

@with_setup(setup_stdout, teardown_stdout)
def test_invoking_help_without_params_shows_default_help():
    command.handle('help')
    content = ''.join(sys.stdout.outputs)

    sys.stdout.outputs = []

    command.print_help(sys.argv[0], 'tip')
    expected = ''.join(sys.stdout.outputs)
    
    assert_equals(expected, content)

@with_setup(setup_stdout, teardown_stdout)
def test_invoking_help_with_param_shows_subcommand_help():
    # Feels weird but we're getting help for the help command
    # to avoid dependency of other commands in this test
    command.handle('help', 'help')
    content = ''.join(sys.stdout.outputs)

    sys.stdout.outputs = []

    from tip.management.commands.tip import ShowHelp
    help_command = ShowHelp()
    help_command.print_help(sys.argv[0], 'tip help')
    expected = ''.join(sys.stdout.outputs)
    
    assert_equals(expected, content)

