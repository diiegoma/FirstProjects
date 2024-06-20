#from cmath import e
#from pytube import YouTube

#def download_video_yt(url, path ='\Users\diiee\Downloads'):
#    try
#       yt = YouTube(url)
#       yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
#       print ("download completed nigga")
#    excepct Exception as e: # type: ignore
#        print ("ERROR:", e)
    
#url_youtube = input ("Give the URL from YT: ")
#path = input ("Give the path (default actual path):")
#download_video_yt (url_youtube, path)
#This was my code

#This one is the corrected code done by the AI        
        
from cmath import e
from pytube import YouTube

def download_video_yt(url, path=r'\Users\diiee\Downloads'):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first()
        stream.download(path)
        print("already installed, ik the quality isn't the best but thats what i do nigga")
    except Exception as e:
        print("ERROR:", e)

url_youtube = input("you skinny bitch give me the link from yt: ")
path = input("give the path where the video should download :")
download_video_yt(url_youtube, path)