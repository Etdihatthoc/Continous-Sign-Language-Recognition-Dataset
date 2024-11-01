import os
import logging
import moviepy.editor as mpy

# Thiết lập logging
log_file = "/mnt/disk4/handsign_project/son_data/a.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")

# Đường dẫn đến thư mục chứa video nguồn và thư mục đích
source_dir = "/mnt/disk4/handsign_project/son_data/Video_scape/22h"
destination_dir = "/mnt/disk4/handsign_project/son_data/Cropped"

# Thiết lập tọa độ cắt
x1 = 0 + 110
y1 = 470
x2 = 190 + 90
y2 = 640

# Đảm bảo thư mục đích tồn tại
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Duyệt qua tất cả các file trong thư mục nguồn
for video_file in os.listdir(source_dir):
    if video_file.endswith((".mp4", ".ts")):
        input_video_path = os.path.join(source_dir, video_file)
        output_video_path = os.path.join(destination_dir, f"cropped_{video_file}")

        try:
            # Tạo đối tượng VideoFileClip từ video nguồn
            video_clip = mpy.VideoFileClip(input_video_path)

            # Cắt video theo tọa độ đã cho
            cropped_clip = video_clip.subclip(0, None).crop(x1=x1, y1=y1, x2=x2, y2=y2)

            # Lưu video đã cắt với codec h264
            cropped_clip.write_videofile(
                output_video_path,
                codec="h264",
                preset="ultrafast",  # Hoặc "fast", "medium"
                threads=48
            )

            # Ghi vào log sau khi hoàn thành
            logging.info(f"Successfully processed {video_file}")

        except Exception as e:
            logging.error(f"Error processing {video_file}: {str(e)}")
