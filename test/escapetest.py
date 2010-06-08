# -*- encoding: UTF-8
## begin license ##
#
#    Copyright (C) 2006-2010 Seek You Too B.V. (CQ2) http://www.cq2.nl
#
#    This file is part of Escaping.
#
#    Escaping is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    Escaping is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Storage; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

from unittest import TestCase

from escaping import escapeFilename

from os.path import join, isfile
from os import remove

class EscapeTest(TestCase):

    def testStrangeCharactersInName(self):
        self.assertName('~!@# $%^&*()\t_<>+\\\f\n\/{}[-]ç«»\'´`äëŝÄ')
        self.assertName('---------')
        self.assertName('sudo rm -rf /*')
        self.assertName('version,v')
        self.assertName('..')
        self.assertName('.')

    def assertName(self, name):
        fname = join( '/tmp', escapeFilename(name))
        open(fname, 'w').close()
        print fname
        try:
            self.assertTrue(isfile(fname))
        finally:
            remove(fname)

    def testEmptyName(self):
        self.assertRaises(ValueError, escapeFilename, '')
