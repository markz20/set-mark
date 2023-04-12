import cv2
import os

# Define video filenames and paths
VIDEO_PATHS = ['deep.mp4', 'cute.mp4']
VIDEO_DIR = ''

# Define function to toggle between videos
def toggle_video(curr_video_index):
    curr_video_index += 1
    if curr_video_index >= len(VIDEO_PATHS):
        curr_video_index = 0
    return curr_video_index

# Initialize variables
curr_video_index = 0
delay_time = 100  # milliseconds

# Create video capture object
cap = cv2.VideoCapture()

# Set video to fullscreen
cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    # Open current video file
    video_path = os.path.join(VIDEO_DIR, VIDEO_PATHS[curr_video_index])
    cap.open(video_path)
    
    while cap.isOpened():
        # Read frame from video
        ret, frame = cap.read()

        if not ret:
            # Video ended, reset to beginning
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        else:
            # Display frame
            cv2.imshow('Video', frame)
            
        # Check for keypress
        key = cv2.waitKey(delay_time)
        if key == 27:
            # Escape key pressed, exit program
            cap.release()
            cv2.destroyAllWindows()
            exit()
        elif key == 32:
            # Spacebar pressed, toggle video
            curr_video_index = toggle_video(curr_video_index)
            cap.release()
            break
