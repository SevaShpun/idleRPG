import codecs
import json
import os

DEFAULT_LOCALE = 'english'

FORM_NOMINATIVE = 1
FORM_GENITIVE = 2  # Родительный падеж
FORM_ABLATIVE = 3  # Творительный падеж
FORM_DEFAULT = 0


# TODO: replace for gettext
class L18n:
    # Class for translation messages to chosen language
    def __init__(self):
        self.locale = ''
        self.encoding = None
        self.msg_map = []
        self.alternative = None

    def set_encoding(self, encoding):
        self.encoding = encoding

    def set_locale(self, name):
        self.locale = name
        f = "l18n//" + name + ".lng"
        fp = codecs.open(f, 'r', "utf-8")
        self.msg_map = json.load(fp)
        if self.locale != DEFAULT_LOCALE:
            self.alternative = L18n()
            self.alternative.set_locale(DEFAULT_LOCALE)

    def get_message(self, msg_type, word_form=None):
        if msg_type in self.msg_map.keys():
            msg = self.msg_map[msg_type]
            if isinstance(msg, dict):
                if word_form == FORM_NOMINATIVE or word_form == FORM_DEFAULT:
                    msg = msg.get("nominative")
                elif word_form == FORM_GENITIVE:
                    msg = msg.get("genitive")
                elif word_form == FORM_ABLATIVE:
                    msg = msg.get("ablative")
                if len(msg) == 0:
                    raise KeyError(
                        "Can't find message {} in locale {} (default locale {} with form {} )".
                            format(msg_type, self.locale, DEFAULT_LOCALE, word_form))
        elif self.locale != DEFAULT_LOCALE:
            msg = self.alternative.get_message(msg_type, word_form)
        else:
            raise KeyError("Can't find message {} in locale {} (default locale {})".format(msg_type, self.locale,
                                                                                           DEFAULT_LOCALE))
        if self.encoding is not None:
            msg = str(msg.encode(self.encoding))
        return msg


class Translator:
    def __init__(self):
        self.locales = {}
        for dirpath, dirnames, filenames in os.walk("l18n"):
            for lang_file in filenames:
                self.locales[lang_file[:2]] = L18n()
                self.locales[lang_file[:2]].set_locale(lang_file[:-4])
        self.default_translator = self.locales["en"]
        self.active_translator = self.default_translator

    def set_locale(self, code):
        if code in self.locales.keys():
            self.active_translator = self.locales[code]
        else:
            self.active_translator = self.default_translator

    def get_message(self, msg_type, code, is_nominative=False, is_genitive=False, is_ablative=False):
        word_form = FORM_DEFAULT
        if is_nominative:
            word_form = FORM_NOMINATIVE
        elif is_genitive:
            word_form = FORM_GENITIVE
        elif is_ablative:
            word_form = FORM_ABLATIVE
        if code in self.locales.keys():
            return self.locales[code].get_message(msg_type, word_form)
        else:
            return self.default_translator.get_message(msg_type, word_form)
