import speech_recognition as sr
from googletrans import Translator, LANGUAGES

def speech_to_text(language='en-US'):
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language=language)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Error: {e}")
        return None

def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text
    return translated_text

def get_language_choice(prompt):
    print(prompt)
    for key, value in LANGUAGES.items():
        print(f"{key}: {value}")
    choice = input("Enter the language code: ").strip().lower()
    if choice in LANGUAGES:
        return choice
    else:
        print("Invalid choice. Defaulting to English (en).")
        return 'en'

if __name__ == "__main__":
    # Prompt the user to select the language for speech input
    input_language = get_language_choice("Please select the language for speech input:")
    
    # Prompt the user to select the target language for translation
    target_language = get_language_choice("Please select the language for translation:")
    
    # Recognize speech and convert to text
    spoken_text = speech_to_text(language=input_language)
    
    if spoken_text:
        # Translate the recognized text to the target language
        translated_text = translate_text(spoken_text, target_language)
        print(f"\nOriginal text: {spoken_text}")
        print(f"Translated text ({target_language}): {translated_text}")

        # Provide the meaning of the speech input in English
        meaning = translate_text(spoken_text, 'en')
        print(f"Meaning of the speech input (in English): {meaning}")