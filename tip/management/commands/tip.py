#!/usr/bin/env python
#-*- coding:utf-8 -*-

# This is needed to avoid a conflict between
# the app named "tip" and the namesake command
from __future__ import absolute_import

from django.core.management.base import BaseCommand, CommandError

from tip.actions import TemplatePathListingAction, TemplateValidationAction, TemplateStructureInfoAction

class Colors():
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    BLUE    = "\033[34m"

class ShowTemplateIncludes(BaseCommand):
    help = "Show templates that includes a template"
    action = TemplateStructureInfoAction()

    def handle(self, *args, **options):
        template = args[0]
        includes = self.action.list_includes(template)
        for include in includes:
            print include

class ShowTemplateList(BaseCommand):
    help = "List templates on the project."
    listing_action      = TemplatePathListingAction()
    validation_action = TemplateValidationAction()
    def handle(self, **options):
        templates_in_paths = self.listing_action.list_all_templates()
        paths = self.listing_action.list_all_paths()
        for path in paths:
            print '%s%s\033[0m' %(Colors.BLUE, path)

            for template in templates_in_paths[path]:
                is_valid, reason = self.validation_action.validate(template)
                color = Colors.GREEN if is_valid else Colors.RED
                print '\t%s%s\033[0m' %(color, template)
                if reason:
                    print reason

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
    args = '<list dirs includes>'
    sub_commands = {
        'list': ShowTemplateList,
        'dirs': ShowTemplateDirs,
        'includes':ShowTemplateIncludes,
    }

    def handle(self, subcommand=None, *args, **kwargs):
        cmd_klass = self.sub_commands.get(subcommand, None)
        if cmd_klass is None:
            raise CommandError('Invalid sub-command "%s".' % subcommand)
        return cmd_klass().execute(*args, **kwargs)
