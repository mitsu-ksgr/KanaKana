# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import sys
from .kanaconverter import to_hiragana, to_katakana, invert_hiragana_katakana

class ConvertToHiraganaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for select in sels:
            s = self.view.substr(select)
            self.view.replace(edit, select, to_hiragana(s))

class ConvertToKatakanaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for select in sels:
            s = self.view.substr(select)
            self.view.replace(edit, select, to_katakana(s))

class InvertHiraganaAndKatakanaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for select in sels:
            s = self.view.substr(select)
            self.view.replace(edit, select, invert_hiragana_katakana(s))
