import os
import logging
import moviepy.editor as mpy

log_file = "/mnt/disk4/handsign_project/son_data/c.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")

source_dir = "/mnt/disk4/handsign_project/son_data/Video_scape/Viet_nam_hom_nay"
destination_dir = "/mnt/disk4/handsign_project/son_data/Cropped"

# Thiết lập tọa độ cắt
x1 = 120
y1 = 460

x2 = 270
y2 = 640

if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

for video_file in os.listdir(source_dir):
    if video_file.endswith((".mp4", ".ts")):
        input_video_path = os.path.join(source_dir, video_file)
        output_video_path = os.path.join(destination_dir, f"cropped_{video_file}")

        try:
            video_clip = mpy.VideoFileClip(input_video_path)

            cropped_clip = video_clip.subclip(0, None).crop(x1=x1, y1=y1, x2=x2, y2=y2)

            cropped_clip.write_videofile(
                output_video_path,
                codec="h264",
                preset="ultrafast",  
                threads=48
            )

            logging.info(f"Successfully processed {video_file}")

        except Exception as e:
            logging.error(f"Error processing {video_file}: {str(e)}")
