#!/usr/bin/env python
#-*- coding:utf-8 -*-

from tip.actions import TemplateStructureInfoAction

def test_i_know_who_includes_a_template():
    i_know_my_template_includes()

def i_know_my_template_includes():
    action = TemplateStructureInfoAction()
    includes = action.list_includes('base_app1.html')
    assert 'included_content/my_content.html' in includes, 'should contain included template'