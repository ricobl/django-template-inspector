#!/usr/bin/env python
#-*- coding:utf-8 -*-

def test_command_infrastructure():
    """basic tests for creating command infrastucture"""
    
    assert i_have_a_tip_module_in_management()
    assert i_have_an_instance_of_tip_command()

def i_have_a_tip_module_in_management():
    from tip.management.commands import tip
    return tip

def i_have_an_instance_of_tip_command():
    from tip.management.commands import tip
    command = tip.Command()
    return command
