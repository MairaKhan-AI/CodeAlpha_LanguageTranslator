from deep_translator import GoogleTranslator

# Decorative line
line = "=" * 50

print(line)
print("      🌍 LANGUAGE TRANSLATOR 🌍")
print(line)

name = input("\nEnter your name: ").strip()

print(f"\nWelcome, {name}! 👋")

while True:

    source = input("\nEnter source language: ").lower().strip()
    target = input("Enter target language: ").lower().strip()
    text = input("Enter text to translate: ").strip()

    try:

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        print("\n" + line)
        print("          TRANSLATION RESULT")
        print(line)

        print(f"\n👤 User: {name}")
        print(f"🌐 Source Language : {source}")
        print(f"🎯 Target Language : {target}")

        print("\nOriginal Text")
        print("-" * 30)
        print(text)

        print("\nTranslated Text")
        print("-" * 30)
        print(translated)

        print(line)

    except Exception:
        print("\n❌ Invalid language or internet connection problem.")

    choice = input("\nTranslate another sentence? (yes/no): ").lower().strip()

    if choice in ["no", "n"]:
        print(f"\n👋 Thank you for using the Language Translator, {name}!")
        break