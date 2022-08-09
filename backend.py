import eel
from pytube import YouTube
eel.init('web')
@eel.expose
def download_video(url):
    yt = YouTube(url)
    video = yt.streams.filter(res="720p").first()
    video.download()
    
eel.start("main.html")