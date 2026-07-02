from deep_translator import GoogleTranslator

print("===== Language Translator =====")

name = input("Enter your name: ")
print(f"\nWelcome, {name}!")

while True:

    source = input("\nEnter source language: ").lower().strip()
    target = input("Enter target language: ").lower().strip()
    text = input("Enter text to translate: ")

    try:
        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        print("\n" + "=" * 50)
        print("          LANGUAGE TRANSLATOR")
        print("=" * 50)

        print(f"\nUser: {name}")
        print(f"Source Language: {source}")
        print(f"Target Language: {target}")

        print("\nOriginal Text")
        print("-" * 30)
        print(text)

        print("\nTranslated Text")
        print("-" * 30)
        print(translated)

        print("=" * 50)

    except Exception:
        print("\nInvalid language code or internet connection problem.")

    choice = input("\nTranslate another sentence? (yes/no): ").lower().strip()

    if choice in ["no", "n"]:
        print(f"\nThank you for using the Language Translator, {name}!")
        break