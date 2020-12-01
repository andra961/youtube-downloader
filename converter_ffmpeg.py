import ffmpeg

'''
This files contains functions to combine video and audio using the ffmpeg-python library,
hoping to obtain a faster method than with moviepy...
HOWEVER IT DOESN'T WORK NOW
'''
# don't call, it seem to not work
def combine_video_and_audio(video_path, audio_path, title, path):
    print("Combining audio and video together...")

    input_video = ffmpeg.input(video_path)

    input_audio = ffmpeg.input(audio_path)

    ffmpeg.output(input_video, input_audio, path + title + ".mp4", vcodec='copy', acodec='aac', strict='experimental').run()

    print("Done")