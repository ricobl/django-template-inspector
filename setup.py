# -*- coding: utf-8 -*-
# <Django Template Inspector - Extracts Information About Django Templates>
# Copyright (C) <2010>  Jose Claudio Figueiredo <jcfigueiredo@gmail.com>
# Copyright (C) <2010>  Enrico Batista <ricobl@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
from tip import __version__

tip_packages=[p for p in find_packages() if p.startswith('tip')]

setup(name='django-tip',
    version=__version__,
    description='Inspector for Django Templates',
    author='Enrico Batista',
    author_email='ricobl@gmail.com',
    url='http://github.com/ricobl/django-template-inspector',
    packages=tip_packages,
    include_package_data = True,
    package_data = {
        'tip': [],
    },
)
