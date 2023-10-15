import os

from moviepy.editor import VideoFileClip

input_directory = "/Users/macbook/Desktop/videos"

output_directory = "/Users/macbook/Desktop/GIFS"
fps = 37.5;

video_files = [f for f in os.listdir(input_directory) if f.endswith(".mp4")]


for filename in video_files:
    input_video_path = os.path.join(input_directory, filename)
    output_gif_path = os.path.join(output_directory, os.path.splitext(filename)[0] + ".gif")

    video_clip = VideoFileClip(input_video_path)
    original_fps = video_clip.fps
    video_clip.close()

    video_clip = VideoFileClip(input_video_path)
    video_clip.write_gif(output_gif_path, fps=fps)
    video_clip.close()


    print(f"Converted {input_video_path} to {output_gif_path} at {fps} FPS")

print("done")
