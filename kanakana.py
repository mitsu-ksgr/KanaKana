# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import sys
from .kanaconverter import to_hiragana, to_katakana, invert_hiragana_katakana

class ConvertToHiraganaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for sel in self.view.sel():
            text = self.view.substr(sel)
            self.view.replace(edit, sel, to_hiragana(text))

class ConvertToKatakanaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for sel in self.view.sel():
            text = self.view.substr(sel)
            self.view.replace(edit, sel, to_katakana(text))

class InvertHiraganaAndKatakanaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for sel in self.view.sel():
            text = self.view.substr(sel)
            self.view.replace(edit, sel, invert_hiragana_katakana(text))
