# coding: utf-8
from __future__ import print_function
import re
from datetime import timedelta
from six.moves import reduce


class ParseError(Exception):
    pass


def parse(s, return_type=int):
    '''
    Parse time string and return seconds.
    You can specify the type of return value both int or datetime.timedelta
    with 'return_type' argument.

    >>> parse('10s')
    10
    >>> parse('1hour5min')
    3900
    >>> from datetime import timedelta
    >>> parse('10s', return_type=timedelta)
    datetime.timedelta(0, 10)
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

    if s is None:
        return None

    if s[-1] in '0123456789':
        s += 's'

    m = re.match(r'^(%s)?(%s)?(%s)?$' % (RE_HOUR, RE_MINUTE, RE_SECOND), s)
    if not m:
        raise ParseError('invalid string: "%s"' % s)

    times = [x for x in m.groups() if isinstance(x, str) and
             re.match(r'[0-9]+[a-z]+', x)]
    seconds = reduce(lambda x, y: x + y,
                     [_parse_time_with_unit(z) for z in times])

    if return_type is int:
        return seconds
    elif return_type is timedelta:
        return timedelta(seconds=seconds)
    else:
        raise TypeError('return_type "{}" is not supported.'.format(
            return_type.__name__))

if __name__ == '__main__':
    print(parse('8minute10'))
