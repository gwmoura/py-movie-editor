from moviepy.editor import *
import moviepy.video.fx.all as vfx

image_clip = ImageClip("image.png", duration=5).set_position('center').fx(vfx.fadeout, 1)

vinheta_end = ImageClip("vinheta_end.png", duration=5).set_position('center').fx(vfx.fadeout, 1)

video = VideoFileClip("video.mkv").subclip(0,13).fx(vfx.fadeout, 1)

result = CompositeVideoClip([image_clip, video.set_start(image_clip.duration).crossfadein(1), vinheta_end.set_start(image_clip.duration+video.duration).crossfadein(1)], size=video.size)
result.write_videofile("my_edited_video.webm", fps=25)
