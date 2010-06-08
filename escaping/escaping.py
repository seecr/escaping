from re import compile

BAD_CHARS = map(chr, range(32)) + ['/', '%', ',']
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

