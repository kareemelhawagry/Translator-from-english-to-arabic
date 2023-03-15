
# Import the required modules
from googletrans import Translator

# Create a translator object with specified service URLs
translator = Translator(service_urls=['translate.google.com'])

# Prompt the user for input
english_text = input("Enter an English word to translate to Arabic: ")

# Use the translator object to translate the text to Arabic
arabic_translation = translator.translate(english_text, src='en', dest='ar')

# Print the translated text
print(f"The Arabic translation of '{english_text}' is '{arabic_translation.pronunciation}'.")
