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
    action = TemplatePathListingAction()

    option_list = BaseCommand.option_list + (
        make_option('-p', '--list_paths', 
            action='store_true', 
            dest='show_templates_path', 
            help=u'List template paths on this project  '),
        make_option('-l', '--list_templates', 
            action='store_true', 
            dest='list_templates', 
            help=u'List templates on this project'),
    )

    def handle(self, *args, **options):
        self.show_templates_path = options.get('show_templates_path')
        self.list_templates = options.get('list_templates')

        if self.show_templates_path:
            self.print_template_paths()
            return

        if self.list_templates:
            self.print_templates()

# \033[32m green
# \033[31m red
# \033[34m blue

    def print_templates(self):
        templates_in_paths = self.action.list_all_templates()
        for path in templates_in_paths.keys():
            print '\033[34m%s\033[0m' %path
            for template in templates_in_paths[path]:
                print '\t\033[32m%s\033[0m' %template

    def print_template_paths(self):
        paths = self.action.list_all_paths()
        
        for path in paths:
            print path
        print "\n"
