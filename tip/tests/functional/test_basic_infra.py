#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import assert_raises
from django.core.management.base import CommandError

def test_command_infrastructure():
    """basic tests for creating command infrastucture"""
    
    assert i_have_a_tip_module_in_management()
    assert i_have_an_instance_of_tip_command()

    tip_command_requires_sub_command()
    tip_command_rejects_unknown_sub_command()

def i_have_a_tip_module_in_management():
    from tip.management.commands import tip
    return tip

def i_have_an_instance_of_tip_command():
    from tip.management.commands.tip import Command
    return Command()

def tip_command_requires_sub_command():
    from tip.management.commands.tip import Command
    assert_raises(CommandError, Command().handle)

def tip_command_rejects_unknown_sub_command():
    from tip.management.commands.tip import Command
    assert_raises(CommandError, Command().handle, 'unknown_sub_command')

