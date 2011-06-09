# Django Template Inspector (tip) 0.0.1

Inspector for Django Templates

## Dependencies

1. django 1.1+ (seems to work on django==1.3)

## Installing

1. Install the python module in your system:

    `pip install django-tip`

2. Add `tip` to the `INSTALLED_APPS` list on your settings (eg: `settings.py`) file:

        INSTALLED_APPS = (
            'django.contrib.auth',
            'django.contrib.admin',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            ...
            'tip',
        )

## Usage

        ./manage.py tip [sub-command]

### Sub-commands

* `./manage.py tip help`: shows available sub-commands
* `./manage.py tip dirs`: lists app and project template dirs
* `./manage.py tip list`: lists all templates in all template dirs
* `./manage.py tip invalid`: lists invalid templates
    * with added verbosity (`-v 2`) displays the error

## Release Plan

* Release 1
    * List all paths defined in `TEMPLATE_DIRS` and all installed apps template dirs.
* Release 2
    * Template listing
    * Template inclusion
* Release 3
    * Invalid template listing
* Release 4
    * Template inheritance (ordered)
* Release 5
    * Template overrides
    * Template Blocks
* Release 6
    * Template Blocks orphans
    * Template Blocks overrides
* Release 7
    * Template Block search
    * Template variables search
* Release 8
    * Web Display of Template information

## Planned Features

1. Template path listing
    * List all paths defined in `TEMPLATE_DIRS` and all installed apps template dirs.
    dirs    List template paths

2. Template structure information
    * Template listing - list option
    * Template inclusion
    * Template inheritance (ordered)
    * Template overrides
    * Template Blocks
    * Template Blocks orphans
    * Template Blocks overrides
    * Template Block search
    * Template variables search
3. Web Display of Template information
4. Template refactoring suggestion
