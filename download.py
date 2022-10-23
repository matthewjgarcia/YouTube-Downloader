from pytube import YouTube
from sys import argv

#use argv to access argument from command line
link = argv[1]

yt = YouTube(link)

# Check if it is the right video
print("The title of the video you want to download is ", yt.title, ". It has ", yt.views, " views.")

#Get highest quality version of video
yd = yt.streams.get_highest_resolution()

# Add to desired folder
yd.download('/Users/mattgarcia/Desktop/youtube_download/dl_yt')
