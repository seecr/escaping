#!/usr/bin/env python
## begin license ##
#
#    Escaping is a collection of functions for escaping filenames etc.
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
import os, sys
os.system('find .. -name "*.pyc" | xargs rm -f')

from glob import glob
for path in glob('../deps.d/*'):
    sys.path.insert(0, path)

sys.path.insert(0, "..")

from unittest import main

from escapetest import EscapeTest

if __name__ == '__main__':
    main()
