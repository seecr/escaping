#!/bin/bash
## begin license ##
#
# Escaping is a collection of functions for escaping filenames etc.
#
# Copyright (C) 2013 Seecr (Seek You Too B.V.) http://seecr.nl
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


export LANG=en_US.UTF-8
export PYTHONPATH=.:"$PYTHONPATH"

pyversions=""
test -e /usr/bin/python2.6 && pyversions="$pyversions python2.6"
test -e /usr/bin/python2.7 && pyversions="$pyversions python2.7"
if [ "${option:0:10}" == "--python2." ]; then
    shift
    pyversions="${option:2}"
fi
echo Found Python versions: $pyversions
for pycmd in $pyversions; do
    echo "================ $pycmd _alltests.py $@ ================"
    $pycmd _alltests.py "$@"
done
