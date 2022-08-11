import eel
from pytube import YouTube
eel.init('web')
@eel.expose
def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(res="720p").first()
        video.download()
    except Exception as e:
        print ("An Error Occured\n", "The Error :\n", e)
    
eel.start("main.html")