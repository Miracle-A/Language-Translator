import googletrans
from googletrans import Translator

# print(googletrans.LANGUAGES)

while True:

    sourceText = input("Enter spanish: ")

    if sourceText == "":
        print("Program has been terminated")
        break

    else:

        translator = Translator()
        result = translator.translate(sourceText, dest='es')

        print(result.text)


