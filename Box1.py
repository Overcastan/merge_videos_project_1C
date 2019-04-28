from moviepy.editor import *
import sys


def main(clip_name1, clip_name2, result_clip_name):
    clip1 = VideoFileClip(clip_name1).subclip()
    clip2 = VideoFileClip(clip_name2).subclip()

    if clip1.duration > clip2.duration:
        clip2 = clip2.volumex(0)
    else:
        clip1 = clip1.volumex(0)

    video = clips_array([[clip1, clip2]])

    video.write_videofile(result_clip_name, temp_audiofile=os.getcwd() + "\\tmpaudio.m4a",
                          audio_codec='aac')


if len(sys.argv) == 4:
    First_clip_name = sys.argv[1]
    Second_clip_name = sys.argv[2]
    Final_clip_name = sys.argv[3]
    main(First_clip_name, Second_clip_name, Final_clip_name)
else:
    print("Incorrect input")
