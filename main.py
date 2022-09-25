from googletrans import Translator


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
    text_translator("Hello my friends!", "fr", "auto")


if __name__ == '__main__':
    main()
