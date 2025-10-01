import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk

from googletrans import Translator, LANGUAGES
from datetime import datetime

# Initialize the Translator
translator = Translator()

def translate_text():
source_text = input_text.get(&quot;1.0&quot;, tk.END).strip()
dest_lang = target_lang_combobox.get().strip()

if not source_text:
messagebox.showerror(&quot;Error&quot;, &quot;Please enter text to translate.&quot;)
return

# Find the language code for the selected language
dest_lang_code = [code for code, lang in LANGUAGES.items() if lang == dest_lang.lower()]
if not dest_lang_code:
messagebox.showerror(&quot;Error&quot;, &quot;Invalid target language.&quot;)
return
dest_lang_code = dest_lang_code[0]

try:
translated = translator.translate(source_text, dest=dest_lang_code)
detected_language = LANGUAGES.get(translated.src, &quot;Unknown&quot;).capitalize()
target_language = dest_lang.capitalize()
translated_text = translated.text
character_count = len(source_text)
timestamp = datetime.now().strftime(&quot;%Y-%m-%d %H:%M:%S&quot;)

# Display translation in GUI
result_text.delete(&quot;1.0&quot;, tk.END)
result_text.insert(tk.END, f&quot;Original Text: {source_text}\n&quot;)
result_text.insert(tk.END, f&quot;Detected Language: {detected_language}\n&quot;)
result_text.insert(tk.END, f&quot;Translated Text ({target_language}): {translated_text}\n&quot;)
result_text.insert(tk.END, f&quot;Character Count: {character_count}\n&quot;)
result_text.insert(tk.END, f&quot;Timestamp: {timestamp}\n&quot;)

# Save to a log file
with open(&quot;translation_log.txt&quot;, &quot;a&quot;, encoding=&quot;utf-8&quot;) as log_file:
log_file.write(&quot;\n--- Translation Log ---\n&quot;)
log_file.write(f&quot;Original Text: {source_text}\n&quot;)
log_file.write(f&quot;Detected Language: {detected_language}\n&quot;)
log_file.write(f&quot;Translated Text ({target_language}): {translated_text}\n&quot;)
log_file.write(f&quot;Character Count: {character_count}\n&quot;)
log_file.write(f&quot;Timestamp: {timestamp}\n&quot;)
log_file.write(&quot;---\n&quot;)
except Exception as e:
messagebox.showerror(&quot;Error&quot;, f&quot;Translation failed: {e}&quot;)

# Create the main window
root = tk.Tk()
root.title(&quot;Advanced Language Translator&quot;)
root.geometry(&quot;600x400&quot;)
root.configure(bg=&quot;#f5f5f5&quot;)

# Input Text Section

input_label = tk.Label(root, text=&quot;Enter text to translate:&quot;, font=(&quot;Arial&quot;, 12), bg=&quot;#f5f5f5&quot;)
input_label.pack(pady=10)
input_text = scrolledtext.ScrolledText(root, height=5, width=60, font=(&quot;Arial&quot;, 10))
input_text.pack(pady=5)

# Target Language Section
target_lang_label = tk.Label(root, text=&quot;Select target language:&quot;, font=(&quot;Arial&quot;, 12),
bg=&quot;#f5f5f5&quot;)
target_lang_label.pack(pady=10)

# Create a list of language options
languages = list(LANGUAGES.values())
languages.sort()

# Dropdown menu for language selection
target_lang_combobox = ttk.Combobox(root, values=languages, width=30, state=&quot;readonly&quot;,
font=(&quot;Arial&quot;, 10))
target_lang_combobox.set(&quot;Select a language&quot;) # Default placeholder
target_lang_combobox.pack(pady=5)

# Translate Button
translate_button = tk.Button(root, text=&quot;Translate&quot;, command=translate_text, font=(&quot;Arial&quot;, 12),
bg=&quot;#4caf50&quot;, fg=&quot;white&quot;, width=15)
translate_button.pack(pady=20)

# Output Section
result_label = tk.Label(root, text=&quot;Translation Results:&quot;, font=(&quot;Arial&quot;, 12), bg=&quot;#f5f5f5&quot;)
result_label.pack(pady=10)
result_text = scrolledtext.ScrolledText(root, height=10, width=60, font=(&quot;Arial&quot;, 10))

result_text.pack(pady=5)

# Run the application
root.mainloop()