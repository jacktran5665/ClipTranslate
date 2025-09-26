import re, time, keyboard, pyperclip, tkinter as tk, queue, threading
from deep_translator import GoogleTranslator
import pystray
from PIL import Image, ImageDraw

class ClipTranslator:
    # ===== LANGUAGE SETTINGS - EDIT THESE =====
    SOURCE_LANG = 'ja'          # Source language code (ja=Japanese, en=English, es=Spanish, etc.)
    TARGET_LANG = 'en'          # Target language code
    DISPLAY_NAME = 'JP→EN'      # Display name for popup header

    # Language detection patterns (add your own if needed)
    DETECTION_PATTERNS = {
        'ja': r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]',  # Japanese
        'ko': r'[\uAC00-\uD7AF]',                            # Korean  
        'zh': r'[\u4E00-\u9FFF]',                            # Chinese
        'ar': r'[\u0600-\u06FF]',                            # Arabic
        'ru': r'[\u0400-\u04FF]',                            # Russian
    }
    # ==========================================
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.queue = queue.Queue()
        self.running = True
        self.tray_icon = None
    
    def detect_source_lang(self, text):
        if self.SOURCE_LANG in self.DETECTION_PATTERNS:
            pattern = self.DETECTION_PATTERNS[self.SOURCE_LANG]
            return bool(re.search(pattern, text))
        return True 

    def translate(self, text):
        text = text.strip()
        if not text: return None, "No text"
        if not self.detect_source_lang(text): 
            return None, f"Text is not in {self.SOURCE_LANG.upper()}"
        try:
            result = GoogleTranslator(source=self.SOURCE_LANG, target=self.TARGET_LANG).translate(text)
            return result, self.DISPLAY_NAME
        except Exception as e:
            return None, f"Error: {e}"

    def drag_start(self, e, popup):
        popup.x, popup.y = e.x_root, e.y_root
        popup.ox, popup.oy = popup.winfo_x(), popup.winfo_y()

    def drag_move(self, e, popup):
        x = popup.ox + (e.x_root - popup.x)
        y = popup.oy + (e.y_root - popup.y)
        popup.geometry(f"350x120+{x}+{y}")

    def show_popup(self, text):
        popup = tk.Toplevel(self.root)
        popup.geometry("350x120")
        popup.configure(bg="#2d2d2d")
        popup.overrideredirect(True)

        popup.update_idletasks()
        x = (popup.winfo_screenwidth() // 2) - 175
        y = popup.winfo_screenheight() - 170
        popup.geometry(f"350x120+{x}+{y}")

        header = tk.Frame(popup, bg="#2d2d2d", height=25, cursor="hand2")
        header.pack(fill="x", padx=8, pady=(5,0))
        header.bind("<Button-1>", lambda e: self.drag_start(e, popup))
        header.bind("<B1-Motion>", lambda e: self.drag_move(e, popup))
        
        tk.Label(header, text=f"🌐 {self.DISPLAY_NAME}", font=("Segoe UI", 9, "bold"), 
                bg="#2d2d2d", fg="#0078d4", cursor="hand2").pack(side="left")
        tk.Button(header, text="✕", font=("Segoe UI", 10), bg="#2d2d2d", 
                 fg="#ffffff", bd=0, command=popup.destroy).pack(side="right")

        txt = tk.Text(popup, font=("Segoe UI", 11), wrap=tk.WORD, relief="flat", 
                     bd=8, bg="#383838", fg="#ffffff", height=4)
        txt.pack(fill="both", expand=True, padx=8, pady=(5,8))
        txt.insert("1.0", text)
        txt.config(state="disabled")
        
        popup.after(8000, popup.destroy)

    def hotkey(self):
        try:
            text = pyperclip.paste()
            if not text.strip():
                return
            
            result, msg = self.translate(text)
            if result:
                self.queue.put(result)
        except:
            pass

    def create_tray_icon(self):
        # Create a simple icon image
        image = Image.new('RGB', (64, 64), color='#0078d4')
        draw = ImageDraw.Draw(image)
        draw.ellipse([16, 16, 48, 48], fill='white')
        draw.text((26, 22), "T", fill='#0078d4', font_size=20)
        
        # Create system tray menu
        menu = pystray.Menu(
            pystray.MenuItem(f"Clipboard Translator ({self.DISPLAY_NAME})", None, enabled=False),
            pystray.MenuItem("Hotkey: Ctrl+Shift+X", None, enabled=False),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Quit", self.quit_app)
        )
        
        self.tray_icon = pystray.Icon("ClipTranslator", image, menu=menu)
    
    def quit_app(self, icon=None, item=None):
        self.running = False
        if self.tray_icon:
            self.tray_icon.stop()
        self.root.quit()
    
    def run_gui(self):
        keyboard.add_hotkey('ctrl+shift+x', self.hotkey)
        
        while self.running:
            try:
                self.root.update()
                try:
                    self.show_popup(self.queue.get_nowait())
                except queue.Empty:
                    pass
                time.sleep(0.01)
            except:
                break
        
        self.root.destroy()
    
    def run(self):
        # Create and start system tray icon in separate thread
        self.create_tray_icon()
        tray_thread = threading.Thread(target=self.tray_icon.run, daemon=True)
        tray_thread.start()
        
        # Run GUI in main thread
        self.run_gui()

if __name__ == "__main__":
    ClipTranslator().run()