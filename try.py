from deep_translator import GoogleTranslator

print("===== Language Translator =====")

name = input("Enter your name: ")
source = input("Enter source language: ")
target = input("Enter target language: ")
text = input("Enter text to translate: ")

try:
    translated = GoogleTranslator(
        source=source,
        target=target
    ).translate(text)

    print(f"\nWelcome, {name}!")
    print("\nOriginal :", text)
    print("Translated:", translated)

except Exception:
    print("\nInvalid language code or internet connection problem.")