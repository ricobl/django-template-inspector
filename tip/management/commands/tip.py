#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.core.management.base import BaseCommand
from django.conf import settings

from optparse import make_option
import pprint

import os
import sys

sys.path.append(os.path.join(settings.ROOT_DIR, "tip"))

from actions import TemplatePathListingAction

class Command(BaseCommand):
    help = u"""
        Show information about templates
"""
    verbose = False

    option_list = BaseCommand.option_list + (
        make_option('-p', '--path_list', 
            action='store_true', 
            dest='show_templates_path', 
            help=u'List template paths'),
    )

    def handle(self, *args, **options):
        self.show_templates_path = options.get('show_templates_path')

        if self.show_templates_path:
            self.print_template_paths()

    def print_template_paths(self):
        action = TemplatePathListingAction()
        paths = action.list_all_paths()
        
        for path in paths:
            print path
        print "\n"
