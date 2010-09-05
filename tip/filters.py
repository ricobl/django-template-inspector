# -*- coding: utf-8 -*-

from tip.actions import TemplateValidationAction

validation_action = TemplateValidationAction()

all = lambda template: True

def invalid(template):
    is_valid, reason = validation_action.validate(template)
    return not is_valid

