#!/usr/bin/env python
#-*- coding:utf-8 -*-

# This is needed to avoid a conflict between
# the app named "tip" and the namesake command
from __future__ import absolute_import

import sys

from django.core.management.base import BaseCommand, CommandError

from tip.actions import TemplatePathListingAction, TemplateValidationAction, TemplateStructureInfoAction

class Colors:
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    BLUE    = "\033[34m"

class ShowTemplateIncludes(BaseCommand):
    help = "Show templates that includes a template"
    action = TemplateStructureInfoAction()

    def handle(self, template, **options):
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

class ShowHelp(BaseCommand):
    help = "Shows help about tip command or sub-command."

    def handle(self, subcommand=None, **options):
        program_name = sys.argv[0]
        if subcommand is None:
            Command().print_help(program_name, 'tip')
            return
        command = Command.get_subcommand(subcommand)
        command.print_help(program_name, 'tip %s' % subcommand)

class Command(BaseCommand):
    help = u"""Show information about templates."""
    args = '<list dirs includes help>'
    sub_commands = {
        'help': ShowHelp,
        'list': ShowTemplateList,
        'dirs': ShowTemplateDirs,
        'includes': ShowTemplateIncludes,
    }

    @classmethod
    def get_subcommand(cls, subcommand):
        cmd_klass = cls.sub_commands.get(subcommand, None)
        if cmd_klass is None:
            raise CommandError('Invalid sub-command "%s".' % subcommand)
        return cmd_klass()

    def handle(self, subcommand=None, *args, **kwargs):
        command = self.get_subcommand(subcommand)
        return command.handle(*args, **kwargs)

    def print_help(self, program_name, subcommand):
        super(Command, self).print_help(program_name, subcommand)
        print '\nAvailable sub-commands:'
        for key, cmd_klass in Command.sub_commands.iteritems():
            print '  %s%s' % (key.ljust(22), cmd_klass.help)
