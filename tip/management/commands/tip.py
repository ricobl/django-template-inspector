#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.core.management.base import BaseCommand
from optparse import make_option

class Command(BaseCommand):
    help = u"""
Show information about templates

"""
    verbose = True

    option_list = BaseCommand.option_list + (
        make_option('-p', '--path_list', 
            action='store_false', 
            dest='show_templates_path', 
            help=u'List template paths'),
    )

    def handle(self, *args, **options):
        self.show_templates_path = bool(options.get('action', False))

    def _show_messsage(self, mensagem):
        if self.verbose:
            print(mensagem)