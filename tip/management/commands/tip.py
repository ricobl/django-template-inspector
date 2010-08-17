#!/usr/bin/env python
#-*- coding:utf-8 -*-

# This is needed to avoid a conflict between
# the app named "tip" and the namesake command
from __future__ import absolute_import

from django.core.management.base import BaseCommand, CommandError

from tip.actions import TemplatePathListingAction

# \033[32m green
# \033[31m red
# \033[34m blue

class ShowTemplateList(BaseCommand):
    help = "List templates on the project."
    action = TemplatePathListingAction()
    def handle(self, **options):
        templates_in_paths = self.action.list_all_templates()
        for path in templates_in_paths.keys():
            print '\033[34m%s\033[0m' %path
            for template in templates_in_paths[path]:
                print '\t\033[32m%s\033[0m' %template

class ShowTemplateDirs(BaseCommand):
    help = "List available template dirs on the project."
    action = TemplatePathListingAction()
    def handle(self, **options):
        paths = self.action.list_all_paths()
        for path in paths:
            print path
        print ""

class Command(BaseCommand):
    help = u"""Show information about templates."""
    args = '<list dirs>'
    sub_commands = {
        'list': ShowTemplateList,
        'dirs': ShowTemplateDirs,
    }

    def handle(self, subcommand, *args, **kwargs):
        cmd_klass = self.sub_commands.get(subcommand, None)
        if cmd_klass is None:
            raise CommandError('Invalid sub-command "%s".' % subcommand)
        return cmd_klass().execute(*args, **kwargs)
