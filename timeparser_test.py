# coding: utf-8
import unittest
from datetime import timedelta
from timeparser import parse, ParseError


class TimeParserTest(unittest.TestCase):
    def test_parse_none(self):
        '''Tests timeparser.parse() when None is passed.
        Returns None.
        '''
        self.assertIsNone(parse(None))

    def test_parse_parse_second(self):
        '''Tests timeparser.parse() when second is passed.
        '''
        self.assertEqual(parse('15second'), 15)

    def test_parse_parse_second_abbrev(self):
        '''Tests timeparser.parse() when second is passed.
        When abbreviation.
        '''
        self.assertEqual(parse('15sec'), 15)
        self.assertEqual(parse('15s'), 15)

    def test_parse_parse_second_without_unit(self):
        '''Tests timeparser.parse() when second is passed.
        When unit is not specified.
        Treats as second.
        '''
        self.assertEqual(parse('43'), 43)

    def test_parse_parse_minute(self):
        '''Tests timeparser.parse() when minute is passed.
        '''
        self.assertEqual(parse('4minute'), 60 * 4)

    def test_parse_parse_minute_abbrev(self):
        '''Tests timeparser.parse() when minute is passed.
        When abbreviation.
        '''
        self.assertEqual(parse('3min'), 60 * 3)
        self.assertEqual(parse('1m'), 60 * 1)

    def test_parse_parse_hour(self):
        '''Tests timeparser.parse() when hour is passed.
        '''
        self.assertEqual(parse('1hour'), 3600 * 1)

    def test_parse_parse_hour_abbrev(self):
        '''Tests timeparser.parse() when hour is passed.
        When abbreviation.
        '''
        self.assertEqual(parse('4h'), 3600 * 4)

    def test_parse_parse_time(self):
        '''Tests timeparser.parse() when complex time string is passed.
        '''
        self.assertEqual(parse('1h50min'), 3600 * 1 + 60 * 50)
        self.assertEqual(parse('17m31s'), 60 * 17 + 31)
        self.assertEqual(parse('11hour45m14sec'), 3600 * 11 + 60 * 45 + 14)
        self.assertEqual(parse('8minute10'), 60 * 8 + 10)
        self.assertEqual(parse('2h5sec'), 3600 * 2 + 5)

    def test_parse_parse_time_error(self):
        '''Tests timeparser.parse() when invalid string is passed.
        Throws timeparser.ParseError.
        '''
        self.assertRaises(ParseError, parse, 'hoge')
        self.assertRaises(ParseError, parse, '1year')
        self.assertRaises(ParseError, parse, 'oooo1')
        self.assertRaises(ParseError, parse, '1has;pgou')

    def test_parse_returns_timedelta(self):
        '''Tests timeparser.parse() with return_value=datetime.timedelta.
        '''
        self.assertEqual(
            parse('1h5min10s', return_type=timedelta),
            timedelta(hours=1, minutes=5, seconds=10)
        )

if __name__ == '__main__':
    unittest.main()
