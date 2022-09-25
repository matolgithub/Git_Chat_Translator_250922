from googletrans import Translator


# class ChatTranslator:
#     def __init__(self, text: str, from_lang: str, to_lang: str):
#         self.text = text
#         self.from_lang = from_lang
#         self.to_lang = to_lang
#
#     def text_translator(self):
#         try:
#             translator = Translator()
#             translation = translator.translate(self, text=self.text, dest=self.to_lang, src=self.from_lang)
#             print(translation)
#             return translation
#         except Exception as ex:
#             print(ex)
#             return ex
#
#     def main(self):
#         text_translator_object = ChatTranslator("Привет", "en", "ru")
#         text_translator_object.text_translator()
#
#
# if __name__ == '__main__':
#     ChatTranslator.main(ChatTranslator)


def text_translator(text, dest, src):
    try:
        translator = Translator()
        translation = translator.translate(text=text, dest=dest, src=src)
        print(translation.text)
        return translation.text
    except Exception as ex:
        print(ex)
        return ex


def main():
    text_translator("Hello my friends!", "ru", "auto")


if __name__ == '__main__':
    main()
