# Clipboard Translator

A lightweight Python tool that instantly translates clipboard text between any languages using a hotkey. Features a clean draggable popup window and customizable language pairs.

## Usage

### Console Version (with output)
1. Run: `python quick_clipboard_translator.py`
2. Copy text in source language `Ctrl+C` for PC | `Cmd+C` 
3. Press `Ctrl+Shift+X` 
4. Translation appears in draggable popup

### Background Version (silent)
1. Run: `start_translator.bat` or double-click `clipboard_translator_bg.pyw`
2. No console window appears - runs silently in background
3. Copy text and press `Ctrl+Shift+X` to translate

### Auto-Start at Boot
**Method - Startup Folder:**
1. Press `Win + R`, type `shell:startup`, press Enter
2. Copy `start_translator.bat` to this folder


## Customization

Edit the language settings at the top of the script:

```python
SOURCE_LANG = 'ja'          # Source language code
TARGET_LANG = 'en'          # Target language code  
DISPLAY_NAME = 'JP→EN'      # Display name
```

## Features

- Any language pair supported by Google Translate
- Auto language detection (Japanese, Korean, Chinese, Arabic, Russian)
- Hotkey: `Ctrl+Shift+X`
- Draggable popup window
- Auto-close after 8 seconds
- Background mode - runs silently without console
- Auto-startup capability

## Installation

Install required packages:
```bash
pip install -r requirements.txt
```

## Requirements

- `deep_translator`, `keyboard`, `pyperclip`, `tkinter`, `pystray`, `Pillow`
- Internet connection
