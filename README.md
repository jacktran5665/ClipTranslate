# Clipboard Translator

Customizable clipboard translator with popup display.

## Usage

1. Run: `python quick_clipboard_translator.py`
2. Copy text in source language `Ctrl+C` for PC | `Cmd+C` for MAC
3. Press `Ctrl+Shift+X` 
4. Translation appears in draggable popup

## Customization

Edit the language settings at the top of the script:

```python
SOURCE_LANG = 'ja'          # Source language code
TARGET_LANG = 'en'          # Target language code  
DISPLAY_NAME = 'JP→EN'      # Display name
```

**Examples:**
- Spanish→English: `SOURCE_LANG = 'es'`, `TARGET_LANG = 'en'`, `DISPLAY_NAME = 'ES→EN'`
- Chinese→English: `SOURCE_LANG = 'zh'`, `TARGET_LANG = 'en'`, `DISPLAY_NAME = 'ZH→EN'`
- English→French: `SOURCE_LANG = 'en'`, `TARGET_LANG = 'fr'`, `DISPLAY_NAME = 'EN→FR'`

## Features

- Any language pair supported by Google Translate
- Auto language detection (Japanese, Korean, Chinese, Arabic, Russian)
- Hotkey: `Ctrl+Shift+X`
- Draggable popup window
- Auto-close after 8 seconds

## Requirements

- `deep_translator`, `keyboard`, `pyperclip`, `tkinter`
- Internet connection