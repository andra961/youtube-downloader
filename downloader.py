import pytube

import converter_moviepy

import os


# remove from title illegal characters found
def clean_title(title):
    illegal_characters = []
    illegal_characters.append('"')
    illegal_characters.append('|')

    for character in illegal_characters:
        title = title.replace(character, "")

    print("New title:" + title)

    return title


# check the resolutions available for the video
def check_available_resolutions(video):

    available_res = []

    print("The available resolutions for this video are:")

    for resolution in ["144p", "240p", "360p", "480p", "720p", "1080p"]:

        if len(video.streams.filter(resolution=resolution, mime_type="video/mp4")) > 0:
            available_res.append(resolution)

            print(resolution)

    return available_res


# download the mp4 video and audio and combine them together
def download_mp4(url, path):

    video = pytube.YouTube(url)

    title = video.title

    title = clean_title(title)

    available_res = check_available_resolutions(video)

    resolution = input("Choose one of the above resolutions:")

    if resolution in available_res:

        print(f'Downloading in {resolution}...')

        # get the proper video stream
        video_stream = video.streams.filter(resolution=resolution, mime_type="video/mp4").first()

        # get the proper audio stream
        audio_stream = video.streams.get_audio_only()

        # download video
        video_path = video_stream.download(filename=f'{title}_video')

        # download audio
        audio_path = audio_stream.download(filename=f'{title}_audio')

        # call the function to combine the downloaded video and audio
        converter_moviepy.combine_video_and_audio(video_path, audio_path, title, path)

        print("Deleting video and audio...")

        # delete downloaded video and audio parts
        os.remove(video_path)
        os.remove(audio_path)

    else:
        print("The inserted resolution is not valid. Closing.")


# download the mp4 video and convert it to mp3
def download_mp3(url, path):

    video = pytube.YouTube(url)

    title = video.title

    title = clean_title(title)

    print("Downloading audio...")

    # download mp4 file
    audio_path = video.streams.get_audio_only().download()

    # call the function to convert it
    converter_moviepy.convert_to_mp3(audio_path, title, path)

    # delete mp4 file
    os.remove(audio_path)
