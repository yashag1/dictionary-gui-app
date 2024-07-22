# simple-dictionary-gui-app

## Description

This is a simple dictionary application built using PySimpleGUI and json libraries of Python and also uses PyAutoGUI for a brief, specific implementation. The app allows users to search for dictionary definitions by typing a word into a search box. Results are displayed in the output area, and ghost text is used as a placeholder in the search box.

## Features

- **Search Box:** Users can type a word into the search box to find its definition.
- **Ghost Text:** The search box displays ghost text ("Start typing the word") that disappears when typing starts.
- **Word Variations:** The application supports variations of the input word by checking for different formats (e.g., hyphenated and concatenated versions).
- **Dynamic Results:** Results for different variations of the input word are shown in the same output area.
- **Error Handling:** Displays messages in red if no match is found or if no input is provided.

## Dictionary Data Source

Instead of using Python's PyDictionary library, this project uses [this](https://github.com/matthewreagan/WebstersEnglishDictionary/blob/master/dictionary.json) JSON copy of the 2009 version of Webster's English dictionary, provided by the [Gutenberg Website](https://www.gutenberg.org/).

## Requirements

- Python 3.x
  - PySimpleGUI
  - json
  - pyautogui (optional, used for simulating key presses)
