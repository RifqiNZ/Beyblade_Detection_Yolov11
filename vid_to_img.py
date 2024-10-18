import cv2
import os

def VideoToFrame (video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        print(f"Error opening video file: {video_path}")
        return
    frame_count = 0
    saved_frame_count = 0
    frame_skip = 10
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        if frame_count % frame_skip == 0:
            resized_frame = cv2.resize(frame, (640, 640))

            frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, resized_frame)
            saved_frame_count += 1
        frame_count += 1
    video_capture.release()
    print(f"Frames extracted and saved to {output_folder}")
video_path = '/Users/rifqinz/Downloads/Kecilin_Test/beyblade3.mp4'
output_folder = '/Users/rifqinz/Downloads/Kecilin_Test/dataBey2'
VideoToFrame(video_path, output_folder)