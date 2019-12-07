import os
from subprocess import call
#music_downloads = "C:/Users/sam/YouTube_Music/"
music_downloads = "/Users/pagel/Desktop/Music/"

os.chdir(music_downloads)
print ('\033[92m' + "Start*******************************************************" + '\033[0m')
youtube_url = raw_input("Paste in youtube url: ")
print("URL pasted was %s" % youtube_url)

command = "youtube-dl --verbose " + youtube_url
print("Attempting command: %s" % command)
#call(command.split(), shell=True)
os.system(command)

print('If failing.. remember to copy the latest youtube-dl to music_downloads location')

# Find name of mp4/webm file and remove spaces and unwanted characters.
for file in os.listdir(music_downloads):
    if file.endswith(".mp4") or file.endswith(".webm") or file.endswith(".mkv"):
        first_name = file
        first_name = first_name.replace(" ", "_")
        os.renames(file, first_name)

first_name = (music_downloads + first_name)
print ('\033[92m' + "Attempt conversion " + first_name + '\033[0m')#print in green here

# Run ffmpeg command and remove .mp4/.webm extension and convert to mp3
command = "ffmpeg -i " + first_name + " -vn -ab 128k -ar 44100 -y " + first_name[:-5] + ".mp3"
#call(command.split(), shell=True)
os.system(command)

# Delete .mp4/.webm ...it's unnessecary
for file in os.listdir(music_downloads):
    if file.endswith(".mp4") or file.endswith(".webm") or file.endswith(".mkv"):
        os.remove(file)

print ('\033[92m' + "SUCCESSFUL CONVERSION!-------------------------------------------------" + '\033[0m')

