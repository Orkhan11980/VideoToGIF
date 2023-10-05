from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("vide.mp4")

videoClip.write_gif("video.gif")