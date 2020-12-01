import moviepy.editor


def combine_video_and_audio(video_path, audio_path, title, path):
    print("Combining audio and video together...")

    video_clip = moviepy.editor.VideoFileClip(video_path)
    audio_clip = moviepy.editor.AudioFileClip(audio_path)

    final_clip = video_clip.set_audio(audio_clip)

    final_clip.write_videofile(filename=path + title + ".mp4")

    video_clip.close()

    audio_clip.close()

    print("Done")


def convert_to_mp3(audio_path, title, path):
    print("Converting to mp3")

    print(audio_path, title)

    audio_clip = moviepy.editor.AudioFileClip(audio_path)

    audio_clip.write_audiofile(filename=path + title + ".mp3")

    audio_clip.close()

    print("Done")
