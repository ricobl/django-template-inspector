#!/usr/bin/env python
#-*- coding:utf-8 -*-

# This is needed to avoid a conflict between
# the app named "tip" and the namesake command
from __future__ import absolute_import

import sys

from django.core.management.base import BaseCommand, CommandError

from tip import filters
from tip.actions import TemplatePathListingAction, TemplateValidationAction, TemplateStructureInfoAction

class Verbosity:
    MINIMAL = 0
    NORMAL = 1
    ALL = 2

class Colors:
    OFF = "\033[0;00m"

    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"

    BOLD_RED = "\033[1;31m"
    BOLD_GREEN = "\033[1;32m"
    BOLD_BLUE = "\033[1;34m"

def color_print(*args):
    print ''.join(args), Colors.OFF

class ShowTemplateIncludes(BaseCommand):
    help = "Show templates that includes a template"
    action = TemplateStructureInfoAction()

    def handle(self, template, **options):
        includes = self.action.list_includes(template)
        for include in includes:
            print include

class ShowTemplateList(BaseCommand):
    help = "List templates on the project."
    listing_action = TemplatePathListingAction()
    validation_action = TemplateValidationAction()

    def print_template(self, template, path):
        is_valid, reason = self.validation_action.validate(template)

        color_name = 'GREEN' if is_valid else 'RED'
        bold_color = getattr(Colors, 'BOLD_%s' % color_name)
        color = getattr(Colors, color_name)

        template = template[len(path):]

        color_print(color, path, bold_color, template)

        if self.verbosity == Verbosity.ALL and reason:
            print reason

    def list_paths(self):
        return self.listing_action.list_all_paths()

    def list_templates(self):
        return self.listing_action.list_all_templates()

    def handle(self, **options):
        self.verbosity = int(options.get('verbosity', 1))
        for template_info in self.list_templates():
            self.print_template(template_info['template'],
                                template_info['path'])

class ShowInvalidTemplateList(ShowTemplateList):
    help = "List invalid templates on the project."

    def list_templates(self):
        return self.listing_action.list_templates(filter=filters.invalid)

class ShowTemplateDirs(BaseCommand):
    help = "List available template dirs on the project."
    action = TemplatePathListingAction()

    def handle(self, **options):
        paths = self.action.list_all_paths()
        for path in paths:
            color_print(Colors.BLUE, path)

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
        'invalid': ShowInvalidTemplateList,
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
