from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os
import string

# Change to the intended directory
FOLD = "./yt/"

# Add all your urls and turns it to a list
yt_urls = []
print("Insert your url and press enter. \nEnter anything when done.")
while True:
    current_url = input()
    if "youtube" in current_url:
        yt_urls.append(current_url)
    else:
        break
print(f"List to download {yt_urls}")


for num, link in enumerate(yt_urls):
    try:
        # Setting up instance and filtering audio dl only
        yt = YouTube(link)
        t = yt.streams.filter(only_audio=True)
        
        # Fixing some naming problems
        # Remove elif statement to remove all punctuations
        # NEED to change the t[0].download file name for stability in that case!!
        name = ""
        for letter in yt.title:
            if letter not in string.punctuation:
                name += letter
            elif letter in "()-":
                name += letter

        # Download the .mp4
        if (name + ".mp4") not in os.listdir(FOLD):
            t[0].download(FOLD)
            print("success")

        # Convert to .mp3
        if (name + ".mp3") not in os.listdir(FOLD):
            audio = AudioFileClip(FOLD + name + ".mp4")
            audio.write_audiofile(f'{FOLD}{name}.mp3')
            audio.close()
    
    except:
        # Exception raised does not necessarily mean the link failed
        # Could be another step
        print(f"Check your url again \n{num}-{link}")
    
    finally:
        # Remove the mp4 if successful
        if (name + ".mp3") in os.listdir(FOLD):
            os.remove(FOLD + name + ".mp4")
            print("Everything was successful")
        # Highlight failed link
        else:
            print(f"Dame da ne dame yo dame na no yo \n{link}")
