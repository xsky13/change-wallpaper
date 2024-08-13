import ctypes
import keyboard
import threading
import random
import time
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# move your images into the image folder
wallpaper_lists = [resource_path("images/image-name"),]


def change_wallpaper():
    path_to_wallpaper = random.choice(wallpaper_lists)
    wallpaper_style = 0 # 0 ==> centered

    SPI_SETDESKWALLPAPER = 20
    image = ctypes.c_wchar_p(path_to_wallpaper)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, wallpaper_style)

def monitor_keys():
    
    time_key_press = 0
    while True:
        delay = 1
        if (keyboard.is_pressed('space')):
            if (time.time() - time_key_press > delay):
                change_wallpaper()
                time_key_press = time.time()
        time.sleep(0.1)

thread = threading.Thread(target=monitor_keys)
thread.daemon = True;
thread.start()

print("Press the space key to change the wallpaper.")
keyboard.wait('|')
