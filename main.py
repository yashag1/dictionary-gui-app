# ISSUES:
# 1. pressing backspace, capslock, shift, etc. inputs a letter in search box
#    when ghost text is being shown
# 2. pressing enter doesn't search
# 3. showing results for {variation name} in same style

# run by: python main.py

import PySimpleGUI as sg
import json
import pyautogui

sg.set_options(font = ('Verdana', 13))
ghost_text = 'Start typing the word'
ghost_text_color = '#A0A0A0'  # Light gray color for the ghost text
default_text_color = '#000000'  # Default black color for regular text

# layout
layout = [
    [sg.InputText(ghost_text, size = (24, 14), key = '-INPUT-', tooltip = 'Type when cursor blinks; click Find to search!', enable_events = True, text_color = ghost_text_color),
     sg.Button('Find', key = '-BTN-')
    ],
    [sg.Multiline(size = (50, 20), key = '-OUTPUT-', disabled = True, autoscroll=True)]
]

# window
window = sg.Window('Dictionary', layout)

# finalize() fully constructs the window before attempting to interact with
# its elements (trying to modify the elements dynamically after app has been loaded)
# in our case - simulating enter presses
window.finalize()

# Simulate pressing backspace twice to solve issue of keys inputting 'd' when pressed for the first time
pyautogui.press('backspace')
pyautogui.press('backspace')

ghost_text_shown = True

# Helper function to check if input is alphanumeric
def is_alpha_input(event, values):
    if event == '-INPUT-' and values['-INPUT-']:
        char = values['-INPUT-'][-1]
        return char.lower().isalpha()
    return False

# loop, events, values
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

#   Clear ghost text on inputting something
    if event == '-INPUT-':
        if ghost_text_shown:
            if is_alpha_input(event, values):

#               Capture the first keystroke and display it manually
                initial_keystroke = values['-INPUT-'][-1]
                window['-INPUT-'].update(initial_keystroke, text_color = default_text_color)
                ghost_text_shown = False
            else:
                window['-INPUT-'].update('')

#   if event == 'Go': would also work, but the button label wouldn't be dynamic then.
    if event == '-BTN-':

        word = values['-INPUT-'].strip().lower()
        if not word or word == ghost_text.lower():
            window['-OUTPUT-'].update('Please enter a word!', text_color = 'red')
            continue

#       Generate variations 'ab', 'a-b' for 'a b' and check if any of these matches.
        word_variants = [word, word.replace(' ', '-'), word.replace(' ', '')]
        
        with open('dictionary.json', 'r') as jf:
            data = json.load(jf)

        results = []
#       Clear the previous output
        window['-OUTPUT-'].update('')

#       Check if the word or its variants are keys in the dictionary
        for variant in word_variants:
            if variant in data:
                if variant != word:
                    window['-OUTPUT-'].update(f'Showing results for {variant}:\n\n', text_color = 'red', append = True)
                results.append(data[variant])
#       append = True makes text appear below already existing text, not replacing it fully

        if results:
            window['-OUTPUT-'].update('\n'.join(results), text_color = 'black', append = True)
        else:
            window['-OUTPUT-'].update('Nothing Found!', text_color = 'red', append = True)

#   To show ghost text when everything is deleted
    if values['-INPUT-'] == '' and not ghost_text_shown:
        window['-INPUT-'].update(ghost_text, text_color = ghost_text_color)
        ghost_text_shown = True

# close
window.close()