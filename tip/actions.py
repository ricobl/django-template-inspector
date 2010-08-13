#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf import settings

class TemplatePathListingAction (object):

    def list_all_paths(self):
        return settings.TEMPLATE_DIRS


