# -*- coding: utf-8 -*-

from django.test import TestCase
from template_inspector import TemplateExplorer

class TemplateExplorerTest(TestCase):

    def test_should_list_available_templates(self):
        explorer = TemplateExplorer()
        template_files = explorer.get_files()
        assert template_files == [
            'base.html',
            'index.html',
        ]

