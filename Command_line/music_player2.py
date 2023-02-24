import random
import os
music_dir = r"C:\Users\HIMANSHU SINGH\Music\download_music"
song =os.listdir(music_dir)
def play():
    n = random.randint(0, 71)
    os.startfile(os.path.join(music_dir,song[n]))
