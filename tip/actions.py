#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf import settings

from django.template.loaders.app_directories import app_template_dirs

from tip.filesystem import FileSystem

class TemplatePathListingAction (object):

    def list_all_paths(self):
        template_paths = settings.TEMPLATE_DIRS

        template_paths += app_template_dirs

        return template_paths

    def list_all_templates(self):
        templates = {}
        paths = self.list_all_paths()
        for path in paths:
            templates[path] = []
            files_in_path = FileSystem.locate(path)
            map(templates[path].append, files_in_path)
        return templates