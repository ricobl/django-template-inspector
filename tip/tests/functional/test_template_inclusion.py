#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
from django.conf import settings
from tip.actions import TemplateStructureInfoAction

def test_i_know_who_includes_a_template():
    i_know_my_template_includes()

def i_know_my_template_includes():
    action = TemplateStructureInfoAction()
    includes = action.list_includes('base_app1.html')
    expected_path = os.path.join(settings.ROOT_DIR,
                                 'dummy_app1/templates/included_content/my_content.html')
    assert expected_path in includes, 'should contain included template'

