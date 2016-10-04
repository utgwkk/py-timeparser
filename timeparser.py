# coding: utf-8
from __future__ import print_function
import re
from six.moves import reduce


class ParseError(Exception):
    pass


def parse(s):
    '''
    Parse time string and return seconds.

    >>> parse('10s')
    10
    >>> parse('1hour5min')
    3900
    '''
    RE_HOUR = r'([0-9]+)h(our)?'
    RE_MINUTE = r'([0-9]+)m(in(ute)?)?'
    RE_SECOND = r'([0-9]+)(s(ec(ond)?)?)?'

    def _parse_time_with_unit(s):
        retval = 0
        mh = re.match(RE_HOUR, s)
        mm = re.match(RE_MINUTE, s)
        ms = re.match(RE_SECOND, s)
        if mh:
            retval = 3600 * int(mh.group(1))
        elif mm:
            retval = 60 * int(mm.group(1))
        elif ms:
            retval = int(ms.group(1))
        return retval

    if isinstance(s, (type(None), int, float)):
        return s

    if s[-1] in '0123456789':
        s += 's'

    m = re.match(r'^(%s)?(%s)?(%s)?$' % (RE_HOUR, RE_MINUTE, RE_SECOND), s)
    if not m:
        raise ParseError('invalid string: "%s"' % s)

    times = [x for x in m.groups() if isinstance(x, str) and
             re.match(r'[0-9]+[a-z]+', x)]
    return reduce(lambda x, y: x + y,
                  [_parse_time_with_unit(z) for z in times])

if __name__ == '__main__':
    print(parse('8minute10'))
