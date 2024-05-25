from pytube import YouTube

link = input("Enter the URL for the video you want to dowload: ")

video = YouTube(link)

stream = video.streams.get_highest_resolution() #helps you download the highest resolution there is

stream.download()
