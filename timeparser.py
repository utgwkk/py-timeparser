# coding: utf-8
import re
from datetime import timedelta


class ParseError(Exception):
    pass


def parse(s, return_type=int):
    '''
    Parse time string and return seconds.
    You can specify the type of return value both int or datetime.timedelta
    with 'return_type' argument.
    '''
    RE_DAY = r'([0-9]+)d(ay)?'
    RE_HOUR = r'([0-9]+)h(our)?'
    RE_MINUTE = r'([0-9]+)m(in(ute)?)?'
    RE_SECOND = r'([0-9]+)(s(ec(ond)?)?)?'

    def _parse_time_with_unit(s):
        retval = 0
        md = re.match(RE_DAY, s)
        mh = re.match(RE_HOUR, s)
        mm = re.match(RE_MINUTE, s)
        ms = re.match(RE_SECOND, s)
        if md:
            retval = 86400 * int(md.group(1))
        elif mh:
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

    m = re.match(r'^(%s)?(%s)?(%s)?(%s)?$' % (RE_DAY, RE_HOUR,
                                              RE_MINUTE, RE_SECOND),
                 s)
    if not m:
        raise ParseError('invalid string: "%s"' % s)

    times = [x for x in m.groups() if isinstance(x, str) and
             re.match(r'[0-9]+[a-z]+', x)]
    seconds = sum(_parse_time_with_unit(z) for z in times)

    if return_type is int:
        return seconds
    elif return_type is timedelta:
        return timedelta(seconds=seconds)
    else:
        raise TypeError('return_type "{}" is not supported.'.format(
            return_type.__name__))
