import cv2

# Load the cat's image
cat_img = cv2.imread('cat.png')

# Load the video
video = cv2.VideoCapture('video-sample.mp4')

# Define the codec and output video file parameters
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = video.get(cv2.CAP_PROP_FPS)
frame_size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, frame_size)

# Load the Haar Cascade classifier
face_cascade = cv2.CascadeClassifier('faces.xml')

# Loop through each video frame and superimpose the cat's face onto detected face regions
while True:
    # Read a frame from the video
    ret, frame = video.read()

    # Break the loop if the video is finished
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the face regions in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Loop through each face region and superimpose the cat's face onto it
    for (x, y, w, h) in faces:
        # Resize the cat's face to the same size as the face region
        cat_face = cv2.resize(cat_img, (w, h))

        # Superimpose the cat's face onto the person's face
        frame[y:y+h, x:x+w] = cv2.addWeighted(frame[y:y+h, x:x+w], 1, cat_face, 0.5, 0)

    # Write the modified frame to the output video file
    out.write(frame)

# Release the video capture and video writer objects
video.release()
out.release()








# video = cv2.VideoCapture("video-sample.mp4")
# cat_face = cv2.imread('cat.png')
# success, frame = video.read()
# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# height = frame.shape[0]
# width = frame.shape[1]
#
# output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))
#
# face_cascade = cv2.CascadeClassifier('faces.xml')
#
# while success:
#     faces = face_cascade.detectMultiScale(frame, 1.3, 5)
#     for(x, y, w, h) in faces:
#         resized_cat_face = cv2.resize(cat_face, (w, h))
#         frame[y:y+w, x:x+w] = cv2.addWeighted(frame[y:y+h, x:x+w], 1, resized_cat_face, 0.5, 0)
#     output.write(frame)
#     success, frame = video.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# output.release()