from pytube import YouTube
link = input("Enter the YouTube video link: ").strip()
video = YouTube(link)
stream = video.streams.get_highest_resolution()

stream.download()
print("Download completed successfully!")
