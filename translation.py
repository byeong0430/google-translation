import requests
import json
import docx # You also need to download python-docx module
from google.cloud import translate
import os, sys

# Variables
# Target language (List of supported languages: https://cloud.google.com/translate/docs/languages)
target_language = 'zh-TW'
input_dir = './input/'
input_file = os.listdir(input_dir)

# Class
class Google:
    def __init__(self, translate):
        self.translate_client = translate.Client()

    def call_translation_api(self, text, target_language):
        tr = self.translate_client.translate(text, target_language)
        return tr['translatedText']

    def translate(self, *args):
        # Destructure array
        text, target_language = args

        # Check if the text parameter type is "string"
        if type(text) != str:
            print('Input: "%s". \nYour input is not a string. Next...' % text)
            return text

        # Remove white space of text
        text = text.strip()
        if not text:
            print('Input: "%s". \nYour input is an empty string. Next...' % text)
            return text
            
        result = self.call_translation_api(text, target_language)
        
        print('"%s" => "%s"' % (text, result))
        return result

# Initialise class
gg = Google(translate)

# Input docx
doc = docx.Document(input_dir + input_file[0])

# Header
for section in doc.sections:
    paragraphs = section.header.paragraphs
    for paragraph in paragraphs:
        if paragraph.text:
            translation = gg.translate(paragraph.text, target_language)
            paragraph.text = translation
        
# Paragraphs
for paragraph in doc.paragraphs:
    if paragraph.text:
        translation = gg.translate(paragraph.text, target_language)
        paragraph.text = translation

# Tables
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            if cell.text:
                translation = gg.translate(cell.text, target_language)
                cell.text = translation

# Footer
for section in doc.sections:
    paragraphs = section.footer.paragraphs
    for paragraph in paragraphs:
        if paragraph.text:
            translation = gg.translate(paragraph.text, target_language)
            paragraph.text = translation

doc.save('./output/translated_' + input_file[0])