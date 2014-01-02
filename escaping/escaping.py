## begin license ##
#
#    Escaping is a collection of functions for escaping filenames etc.
#
#    Copyright (C) 2006-2010 Seek You Too B.V. (CQ2) http://www.cq2.nl
#    Copyright (C) 2012 Seecr (Seek You Too B.V.) http://seecr.nl
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
from re import compile

BAD_CHARS = list(map(chr, list(range(32)))) + ['/', '%', ',']
FIND_BAD_CHARS = compile('(^\.|' + '|'.join(BAD_CHARS)+')')
CHAR_TO_HEX = lambda x: '%%%02X' % ord(x.group(1))

HEX_TO_CHAR = lambda x:chr(int(x.group(1),16))
REVERSE_BAD_CHARS = compile('%([0-9A-F]{2})')

BAD_BASH_CHARS = ['!','@','$','&','<','>', '|', '(',')',';', '*', '`', '\'', '"', '\\', ' ']

CHARS_FOR_RANDOM = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890'

def escapeFilename(name):
    if not name:
        raise ValueError('filename is empty')
    return FIND_BAD_CHARS.sub(CHAR_TO_HEX, name)

def unescapeFilename(name):
    return REVERSE_BAD_CHARS.sub(HEX_TO_CHAR, name)

def bashEscape(name):
    return ''.join((char in BAD_BASH_CHARS and '\\' + char or char for char in name))

