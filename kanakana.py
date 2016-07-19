# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import sys
from . import kanaconverter

class ConvertToHiraganaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for sel in self.view.sel():
            text = self.view.substr(sel)
            self.view.replace(edit, sel, kanaconverter.to_hiragana(text))

class ConvertToKatakanaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for sel in self.view.sel():
            text = self.view.substr(sel)
            self.view.replace(edit, sel, kanaconverter.to_katakana(text))

class InvertHiraganaAndKatakanaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for sel in self.view.sel():
            text = self.view.substr(sel)
            self.view.replace(edit, sel, kanaconverter.invert_hiragana_katakana(text))
