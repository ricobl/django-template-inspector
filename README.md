# Django Template Inspector (tip) 0.0.1

Inspector for Django Templates

## Dependencies

1. django 1.1+

## Installing

1. Install the python module in your system:

    `python setup.py install`

2. Install the app within your django project by editing your `settings.py` file:

    `INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.admin',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        ...
        'tip',
    )`

## Release Plan

* Release 1
    * List all paths defined in `TEMPLATE_DIRS` and all installed apps template dirs.
* Release 2
    * Template listing
    * Template inclusion
* Release 3
    * Template inheritance (ordered)
* Release 4
    * Template overrides
    * Template Blocks
* Release 5
    * Template Blocks orphans
    * Template Blocks overrides
* Release 6
    * Template Block search
    * Template variables search
    * Web Display of Template information

## Planned Features

1. Template path listing
    * List all paths defined in `TEMPLATE_DIRS` and all installed apps template dirs.
2. Template structure information
    * Template listing
    * Template inheritance (ordered)
    * Template inclusion
    * Template overrides
    * Template Blocks
    * Template Blocks orphans
    * Template Blocks overrides
    * Template Block search
    * Template variables search
3. Web Display of Template information

