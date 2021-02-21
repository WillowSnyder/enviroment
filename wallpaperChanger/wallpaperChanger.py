import os
import time
import random

wallpaper_path = "/home/wyatt/Pictures/Wallpapers/"
base_command = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri "
sleep_time = 5

# Rename all wallpapers to avoid bugs with the names
while True:
    print("Checking dir for new pictures")
    wallpapers = os.listdir(wallpaper_path)
    wallpapers.sort()

    print("renaming pictures")
    for i in range(len(wallpapers)):
        new_name = str(i).zfill(3) + "." + wallpapers[i].split('.')[1]
        os.rename(wallpaper_path + wallpapers[i], wallpaper_path + new_name)
        wallpapers[i] = new_name

    print("shuffling pictures")
    random.shuffle(wallpapers)

    print("displaying pictures")
    for wallpaper in wallpapers:
        os.system(base_command + wallpaper_path + wallpaper)
        time.sleep(sleep_time)
