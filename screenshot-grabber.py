import os
import random
import urllib.request
import imageio
from moviepy.video.io.VideoFileClip import VideoFileClip

# File containing the video URLs. One URL per line.
video_urls_file = 'video_urls.txt'

# The directory to save the screenshots
screenshot_dir = 'screenshots'

# Create the directory if it doesn't exist
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

# Let's get the list of video URLs from the file
with open(video_urls_file, 'r') as f:
    video_urls = f.readlines()
    video_urls = [url.strip() for url in video_urls]

# Time to iterate through the list of video URLs
for url in video_urls:
    # Download the video
    video_filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, video_filename)

    # Open it
    video = VideoFileClip(video_filename)

    # Generate a random time to take the screenshot from and get the screenshot
    screenshot_time = random.uniform(0, video.duration)
    screenshot = video.get_frame(screenshot_time)

    # Save the screenshot
    screenshot_filename = f'{screenshot_dir}/screenshot_{video_filename}.png'
    imageio.imwrite(screenshot_filename, screenshot)

    # Remove the video becase we don't need it anymore
    os.remove(video_filename)
