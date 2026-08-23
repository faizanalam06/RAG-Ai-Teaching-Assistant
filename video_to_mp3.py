# convert video to mp3

import os
import subprocess

os.makedirs('audios',exist_ok=True)
files  = os.listdir('Video')



for index, file in enumerate(files, start=1):
    tutorial_name = file.split(".")[0]

    
    print(f"{index} {tutorial_name}")
    subprocess.run(["ffmpeg", "-i",f"Video/{file}",f"audios/{index} {tutorial_name}.mp3"])
    print("the mp3 is download succssfully")