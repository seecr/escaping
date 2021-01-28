## begin license ##
#
# Escaping is a collection of functions for escaping filenames etc.
#
# Copyright (C) 2006-2010 Seek You Too B.V. (CQ2) http://www.cq2.nl
# Copyright (C) 2013, 2020-2021 Seecr (Seek You Too B.V.) https://seecr.nl
# Copyright (C) 2020-2021 Data Archiving and Network Services https://dans.knaw.nl
# Copyright (C) 2020-2021 SURF https://www.surf.nl
# Copyright (C) 2020-2021 Stichting Kennisnet https://www.kennisnet.nl
# Copyright (C) 2020-2021 The Netherlands Institute for Sound and Vision https://beeldengeluid.nl
#
# This file is part of "Escaping"
#
# "Escaping" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# "Escaping" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Escaping"; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

from distutils.core import setup

setup(
    name='escaping',
    packages=['escaping'],
    version='%VERSION%',
    url='https://seecr.nl',
    author='Seecr',
    author_email='info@seecr.nl',
    description='A collection of routines to escape identifiers',
    long_description='A collection of routines to escape identifiers.',
    license='GNU Public License',
    platforms='all',
)
