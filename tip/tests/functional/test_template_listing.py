#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import assert_equals, assert_not_equals

from django.conf import settings
from tip.tests.helpers import abs

from tip.actions import TemplatePathListingAction

action = TemplatePathListingAction()
paths = action.list_all_paths()


def test_retrieving_path_based_on_setting():
    i_have_template_dirs_defined_in_settings()

def i_have_template_dirs_defined_in_settings():
    from django.conf import settings
    assert settings.TEMPLATE_DIRS

def test_i_can_list_all_templates_defined_in_the_settings_file():
    i_have_a_template_folder_on_my_path()

def i_have_a_template_folder_on_my_path():
    assert abs(settings.ROOT_DIR, 'templates') in paths, 'should have a template folder on ROOT_DIR'

def test_i_have_installed_apps_template_folders_on_my_path():
    assert abs(settings.ROOT_DIR, 'dummy_app1/templates') in paths, 'should have the template folder for DUMMY_APP1'
    assert abs(settings.ROOT_DIR, 'dummy_app2/templates') not in paths, 'should have the template folder for DUMMY_APP1'

