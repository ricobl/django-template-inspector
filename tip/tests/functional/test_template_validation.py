#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import assert_equals
from tip.actions import TemplateValidationAction

action = TemplateValidationAction()

def test_i_know_whether_a_template_is_valid_or_not():
    i_know_when_a_template_is_invalid()
    i_know_when_a_template_is_valid()

def i_know_when_a_template_is_invalid():
    
    is_valid, reason = action.validate('invalid_template.html')

    assert_equals(is_valid, False, 'Should evaluate as an invalid template')
    assert_equals(reason, "Unclosed tag 'block'. Looking for one of: endblock, endblock 'invalid' ", 
        'Should have a reason because template is invalid')

def i_know_when_a_template_is_valid():

    is_valid, reason = action.validate('base_app1.html')
    assert_equals(is_valid, True, 'Should evaluate as a valid template')
    assert_equals(reason, None, 'Should have NO reason because template is valid')
