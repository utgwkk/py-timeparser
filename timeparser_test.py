# coding: utf-8
import unittest
from timeparser import parse, ParseError


class TimeParserTest(unittest.TestCase):
    def test_parse_none(self):
        '''引数に None が渡された場合の parse のテスト。
        None を返す。
        '''
        self.assertIsNone(parse(None))

    def test_parse_parse_second(self):
        '''秒のみ指定された場合の parse のテスト。
        '''
        self.assertEqual(parse('15second'), 15)

    def test_parse_parse_second_abbrev(self):
        '''秒のみ指定された場合の parse のテスト。
        単位が省略形の場合。
        '''
        self.assertEqual(parse('15sec'), 15)
        self.assertEqual(parse('15s'), 15)

    def test_parse_parse_second_without_unit(self):
        '''秒のみ指定された場合の parse のテスト。
        単位がない場合。
        '''
        self.assertEqual(parse('43'), 43)

    def test_parse_parse_minute(self):
        '''分のみ指定された場合の parse のテスト。
        '''
        self.assertEqual(parse('4minute'), 60 * 4)

    def test_parse_parse_minute_abbrev(self):
        '''分のみ指定された場合の parse のテスト。
        単位が省略形の場合。
        '''
        self.assertEqual(parse('3min'), 60 * 3)
        self.assertEqual(parse('1m'), 60 * 1)

    def test_parse_parse_hour(self):
        '''時のみ指定された場合の parse のテスト。
        '''
        self.assertEqual(parse('1hour'), 3600 * 1)

    def test_parse_parse_hour_abbrev(self):
        '''時のみ指定された場合の parse のテスト。
        単位が省略形の場合。
        '''
        self.assertEqual(parse('4h'), 3600 * 4)

    def test_parse_parse_time(self):
        '''秒・分・時が指定された場合の parse のテスト。
        '''
        self.assertEqual(parse('1h50min'), 3600 * 1 + 60 * 50)
        self.assertEqual(parse('17m31s'), 60 * 17 + 31)
        self.assertEqual(parse('11hour45m14sec'), 3600 * 11 + 60 * 45 + 14)
        self.assertEqual(parse('8minute10'), 60 * 8 + 10)
        self.assertEqual(parse('2h5sec'), 3600 * 2 + 5)

    def test_parse_parse_time_error(self):
        '''不正な文字列が指定された場合の parse のテスト。
        例外を送出する。
        '''
        self.assertRaises(ParseError, parse, 'hoge')
        self.assertRaises(ParseError, parse, '1year')
        self.assertRaises(ParseError, parse, 'oooo1')
        self.assertRaises(ParseError, parse, '1has;pgou')


if __name__ == '__main__':
    unittest.main()
