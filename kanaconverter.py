#!/usr/bin/env python
# -*- coding: utf-8 -*-

_HIRAGANA_FIRST, _HIRAGANA_END = ord(u'\u3041'), ord(u'\u3096')
_KATAKANA_FIRST, _KATAKANA_END = ord(u'\u30A1'), ord(u'\u30F6')
_CONVERT_OFFSET = ord(u'\u0060')


def _to_hiragana(katakana_char):
    """ Return a hiragana corresponding to a katakana specified in args.
    If args character is not katakana then return as it is.
    """
    d = ord(katakana_char)
    return chr(d - _CONVERT_OFFSET) if _KATAKANA_FIRST <= d <= _KATAKANA_END else katakana_char

def _to_katakana(hiragana_char):
    """ Return a katakana corresponding to a hiragana specified in args.
    If args character is not hiragana then return as it is.
    """
    d = ord(hiragana_char)
    return chr(d + _CONVERT_OFFSET) if _HIRAGANA_FIRST <= d <= _HIRAGANA_END else hiragana_char

def to_hiragana(s, encode = 'utf-8'):
    """ The katakana in a string convert to hiragana.
    Non-katakana characters in the arg string will not converted.
    """
    return ''.join([_to_hiragana(s[i]) for i in range(0, len(s))])

def to_katakana(s):
    """ The hiragana in a string convert to katakana.
    Non-hiragana characters in the arg string will not converted.
    """
    return ''.join([_to_katakana(s[i]) for i in range(0, len(s))])

def invert_hiragana_katakana(s):
    """ Inverts Hiragana/Katakamuna in the string.
    Other than Hiragana and Katakana is not converted.
    """
    ret = []
    for i in range(0, len(s)):
        d = ord(s[i])
        if _HIRAGANA_FIRST <= d <= _HIRAGANA_END:
            ret.append(chr(d + _CONVERT_OFFSET))
        elif _KATAKANA_FIRST <= d <= _KATAKANA_END:
            ret.append(chr(d - _CONVERT_OFFSET))
        else:
            ret.append(s[i])
    return ''.join(ret)


if __name__ == '__main__':
    import unittest
    class KanaConverterTest(unittest.TestCase):
        def setUp(self):
            pass

        def test_to_hiragana(self):
            self.assertEqual(to_hiragana(u'アイウエオヱヴァヶ'), u'あいうえおゑゔぁゖ')
            self.assertEqual(to_hiragana(u'あいうえお'), u'あいうえお')
            self.assertEqual(to_hiragana(u'か木Kuケ子'), u'か木Kuけ子')

        def test_to_katakana(self):
            self.assertEqual(to_katakana(u'あいうえおゑゔぁゖ'), u'アイウエオヱヴァヶ')
            self.assertEqual(to_katakana(u'アイウエオ'), u'アイウエオ')
            self.assertEqual(to_katakana(u'か木Kuケ子'), u'カ木Kuケ子')

        def test_to_invert(self):
            self.assertEqual(invert_hiragana_katakana(u'あいうえおゑゔぁゖ'), u'アイウエオヱヴァヶ')
            self.assertEqual(invert_hiragana_katakana(u'あいうエオ'), u'アイウえお')
            self.assertEqual(invert_hiragana_katakana(u'か木Kuケ子'), u'カ木Kuけ子')
    unittest.main()

