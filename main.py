import yt_dlp

def Download(link, options):
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download(link)
        
link = input("insira a url do video que deseja baixar: ")
options = {
    "format": 'best'
}

Download(link, options)