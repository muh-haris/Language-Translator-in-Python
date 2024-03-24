import tkinter as tk
from googletrans import Translator

# Dictionary mapping language codes to full names
language_names = {
    'fr': 'French',
    'en': 'English',
    'it': 'Italian',
    'es': 'Spanish',
    'ru': 'Russian',
    'de': 'German',
    'ur': 'Urdu',
    'ur-rom': 'Roman Urdu'
}

def translate_text():
    text_to_translate = text_entry.get()
    source_language = next(key for key, value in language_names.items() if value == src_lang_var.get())
    source_language = 'ur' if source_language == 'ur-rom' else source_language
    destination_language = next(key for key, value in language_names.items() if value == dest_lang_var.get())

    if source_language in language_names.keys() and destination_language in language_names.keys():
        translator = Translator()
        translation = translator.translate(text_to_translate, src=source_language, dest=destination_language)
        translated_text_label.config(text=f'Translation from {language_names[source_language]} to {language_names[destination_language]}: {translation.text}')
    else:
        translated_text_label.config(text='Invalid language selection. Please select valid languages.')

# Create the main window
root = tk.Tk()
root.title('Language Translator')

# Create and place widgets
text_label = tk.Label(root, text='Enter text to translate:')
text_label.pack()

text_entry = tk.Entry(root, width=50)
text_entry.pack()

src_lang_label = tk.Label(root, text='Select source language:')
src_lang_label.pack()

src_lang_var = tk.StringVar(root)
src_lang_var.set('English')  # Default source language

src_lang_dropdown = tk.OptionMenu(root, src_lang_var, *list(language_names.values()))
src_lang_dropdown.pack()

dest_lang_label = tk.Label(root, text='Select destination language:')
dest_lang_label.pack()

dest_lang_var = tk.StringVar(root)
dest_lang_var.set('French')  # Default destination language

dest_lang_dropdown = tk.OptionMenu(root, dest_lang_var, *list(language_names.values()))
dest_lang_dropdown.pack()

translate_button = tk.Button(root, text='Translate', command=translate_text)
translate_button.pack()

translated_text_label = tk.Label(root, text='', wraplength=400)
translated_text_label.pack()

# Run the application
root.mainloop()
