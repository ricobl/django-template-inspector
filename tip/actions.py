#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf import settings

from django.template.loaders.app_directories import app_template_dirs
from django.template.loader import get_template
from django.template.loader_tags import ConstantIncludeNode
from tip.filesystem import FileSystem

class TemplatePathListingAction (object):

    def list_all_paths(self):
        template_paths = settings.TEMPLATE_DIRS

        template_paths += app_template_dirs

        return template_paths

    def iter_templates(self, filter):
        for path in self.list_all_paths():
            for template in FileSystem.locate(path):
                if filter(template):
                    yield {'path': path, 'template': template}

    def list_templates(self, filter):
        return list(self.iter_templates(filter))

    def list_all_templates(self):
        return self.list_templates(filter=lambda template: True)

class TemplateValidationAction(object):

    def validate(self, template):

        is_valid = True
        reason = None
        try:
            get_template(template)
        except Exception, ex:
            is_valid = False
            reason = unicode(ex)

        return is_valid, reason


class TemplateStructureInfoAction(object):
    def list_includes(self, template):
        template_object = get_template(template)

        includes = [node.template.name for node in template_object.nodelist if isinstance(node, ConstantIncludeNode)]
        return includes
