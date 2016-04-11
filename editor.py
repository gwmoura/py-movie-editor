from moviepy.editor import *
import moviepy.video.fx.all as vfx
import sys
from optparse import OptionParser

usage = "usage: %prog [options]"
parser = OptionParser(usage=usage)

parser.add_option("--iv", dest="initial_vignette", default="initial_vignette.png", help="Add initial vignette to video [default: %default]")
parser.add_option("--ev", dest="end_vignette", default="end_vignette.png", help="Add end vignette to video [default: %default]")
parser.add_option("--evv", dest="event_vignette", help="Add event vignette to video, this vignette will be added before video start")
parser.add_option("-v", dest="video", default="video.mkv", help="Add video file [default: %default]")
parser.add_option("-o", dest="output_file", help="Output video file name")
parser.add_option("--fps", dest="fps", default=25, help="inform video fps [default: %default]")

(options, args) = parser.parse_args()

if(options.output_file is None):
   sys.exit("You need inform -o option")

if options.initial_vignette is not None:
  initial_vignette = ImageClip(options.initial_vignette, duration=5).set_position('center').fx(vfx.fadeout, 1)

if options.event_vignette is not None:
  event_vignette = ImageClip(options.event_vignette, duration=5).set_position('center').fx(vfx.fadeout, 1)

if options.end_vignette is not None:
  end_vignette = ImageClip(options.end_vignette, duration=5).set_position('center').fx(vfx.fadeout, 1)

if options.video is not None:
  video = VideoFileClip(options.video).fx(vfx.fadeout, 1)

if options.event_vignette is None:
  clips = [initial_vignette, video.set_start(initial_vignette.duration).crossfadein(1), end_vignette.set_start(initial_vignette.duration+video.duration).crossfadein(1)]
else:
  clips = [initial_vignette, event_vignette.set_start(initial_vignette.duration), video.set_start(initial_vignette.duration+event_vignette.duration).crossfadein(1), end_vignette.set_start(initial_vignette.duration+event_vignette.duration+video.duration).crossfadein(1)]

result = CompositeVideoClip(clips, size=video.size)
result.write_videofile(options.output_file, options.fps)
