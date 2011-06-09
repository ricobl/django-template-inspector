#!/usr/bin/env python
#-*- coding:utf-8 -*-

# This is needed to avoid a conflict between
# the app named "tip" and the namesake command
from __future__ import absolute_import

import sys

from django.core.management.base import BaseCommand, CommandError
from django.utils.termcolors import colorize

from tip import filters
from tip.actions import (TemplatePathListingAction, TemplateValidationAction,
        TemplateStructureInfoAction, break_path_and_template)

class Verbosity:
    MINIMAL = 0
    NORMAL = 1
    ALL = 2


def safe_colorize(text='', opts=(), **kwargs):
    is_tty = sys.stdout.isatty()
    if is_tty:
        return colorize(text=text, opts=opts, **kwargs)
    else:
        return text

class ShowTemplateIncludes(BaseCommand):
    help = "Show templates that includes a template"
    action = TemplateStructureInfoAction()

    def handle(self, template='', **options):
        if not template:
            print safe_colorize('include command requires a template', fg='red')
            raise SystemExit
        includes = self.action.list_includes(template)
        for include in includes:
            path, include_template = break_path_and_template(include)
            print safe_colorize(path, fg='yellow') + safe_colorize(include[len(path):], opts=('bold',), fg='yellow')


class ShowTemplateList(BaseCommand):
    help = "List templates on the project."
    listing_action = TemplatePathListingAction()
    validation_action = TemplateValidationAction()

    def print_template(self, template, path):
        is_valid, reason = self.validation_action.validate(template)

        color = 'green' if is_valid else 'red'

        template = template[len(path):]

        print safe_colorize(path, fg=color) + safe_colorize(template, opts=('bold',), fg=color)

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
            print safe_colorize(path, fg='blue')

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
