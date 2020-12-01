import downloader

# the path in which the final result will be downloaded

# example path: "C:\\Users\\user\\Desktop\\youtube_videos\\"

print('''

What to do?

1)Download mp4 video from URL
2)Download mp3 audio from URL
3)Exit

''')

choice = (input("Insert 1 or 2"))

if choice in ["1", "1)"]:
    videoName = input("Insert video URL")
    path = input("Insert path where to download: ")
    downloader.download_mp4(videoName, path)

elif choice in ["2", "2)"]:
    videoName = input("Insert video URL")
    path = input("Insert path where to download: ")
    downloader.download_mp3(videoName, path)

elif choice in ["3", "3)"]:
    print("Closing...")

else:
    print("The choice is not valid...Closing")
