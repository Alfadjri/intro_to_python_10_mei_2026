import os
import subprocess
import sys
from pathlib import Path
import time

try:
    from dotenv import load_dotenv
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv","--break-system-packages"])
    from dotenv import load_dotenv

env_path = Path(__file__).parent / '.env'
if not env_path.exists():
    with open(env_path, 'w') as f:
        f.write("INSTALLED_TKINTER=False\n")
load_dotenv(dotenv_path=env_path)
installed_tkinter = os.getenv("INSTALLED_TKINTER", "False").lower() == "true"

try:
    import tkinter as tk
    from tkinter import messagebox
    tkinter_available = True
except ImportError:
    tkinter_available = False

if not installed_tkinter and not tkinter_available:
    print("Tkinter is not installed. Please install it to run the GUI.")
    try:
        if sys.platform.startswith('linux'):
            subprocess.check_call([sys.executable, "-m", "pip", "install", "tk","--break-system-packages"])
        elif sys.platform.startswith('win'):
            subprocess.check_call([sys.executable, "-m", "pip", "install", "tk","--break-system-packages"])
        elif sys.platform.startswith('darwin'):
            subprocess.check_call([sys.executable, "-m", "pip", "install", "tk","--break-system-packages"])
    except Exception as e:
        print(f"Failed to install Tkinter: {e}")
    
    with open(env_path, 'w') as f:
        f.write("INSTALLED_TKINTER=True\n")

try:
    import tkinter as tk
    from tkinter import messagebox
    def tampilan_popup():
        root = tk.Tk()
        root.withdraw()
        while True:
            popup = tk.Toplevel()
            popup.withdraw()
            popup.attributes("-topmost", True)
            popup.after(0, lambda: popup.focus_force())

            keluar = messagebox.askyesno("Peringatan!", "Apakah Anda yakin ingin keluar?",parent=popup)

            if keluar:
                print("Keluar dari program.")
                popup.destroy()
                root.destroy()
                time.sleep(1)
                tampilan_popup()
                break
            else:
                print("Lanjutkan program.")
                tampilan_popup()
                break
            popup.destroy()
        root.destroy()

    if __name__ == "__main__":
        tampilan_popup()
except Exception as e:
    print(f"An error occurred: {e}")
