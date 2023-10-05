from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("vide.mov")

videoClip.write_gif("video.gif")