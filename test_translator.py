#!/usr/bin/env python3
"""
Test script for Quick Clipboard Translator
This script demonstrates the translation functionality without hotkeys.
"""

import pyperclip
from quick_clipboard_translator import QuickClipboardTranslator

def test_translation():
    """Test the translation functionality with sample texts."""
    
    translator = QuickClipboardTranslator()
    
    # Sample texts for testing
    test_cases = [
        ("Hello World", "English to Japanese"),
        ("こんにちは世界", "Japanese to English"),
        ("I love programming", "English to Japanese"),
        ("プログラミングが大好きです", "Japanese to English"),
        ("Good morning", "English to Japanese"),
        ("おはようございます", "Japanese to English")
    ]
    
    print("🧪 Testing Quick Clipboard Translator\n")
    
    for i, (text, description) in enumerate(test_cases, 1):
        print(f"Test {i}: {description}")
        print(f"Original: {text}")
        
        # Set clipboard
        pyperclip.copy(text)
        
        # Translate
        translated, status = translator.translate_text(text)
        
        if translated:
            print(f"Translated: {translated}")
            print(f"Status: {status}")
        else:
            print(f"Error: {status}")
        
        print("-" * 50)

if __name__ == "__main__":
    test_translation()