import os

from moviepy.editor import VideoFileClip

input_directory = "Path/t/videos"

output_directory = "Path/to/GIFS"

video_files = [f for f in os.listdir(input_directory) if f.endswith(".mp4")]

for filename in video_files:
    input_video_path = os.path.join(input_directory, filename)
    output_gif_path = os.path.join(output_directory, os.path.splitext(filename)[0] + ".gif")
    video_clip = VideoFileClip(input_video_path)
    video_clip.write_gif(output_gif_path)

video_clip.close()

print(f"Converted {input_video_path} to {output_gif_path}")
