import cv2 
import face_recognition
import numpy as np
import dlib

# Initialize known face encodings and names
known_face_encodings = []
known_face_names = []

# Load images and get face encodings
# known_person1_image = face_recognition.load_image_file('madhu_hbd.jpg')
# known_person2_image = face_recognition.load_image_file('hbd_tarun.jpg')
# known_person3_image = face_recognition.load_image_file('chotu.jpg')

img=cv2.imread("madhu_hbd.jpg")
rgb_img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Use COLOR_BGR2RGB, not GRAY for face recognition
img=cv2.imread("hbd_tarun.jpg")
rgb_img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Use COLOR_BGR2RGB, not GRAY for face recognition
img=cv2.imread("chotu.jpg")
rgb_img3 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Use COLOR_BGR2RGB, not GRAY for face recognition
# cv2.imshow('cat',img)
cv2.waitKey(0)

known_person1_encoding = face_recognition.face_encodings(rgb_img1)
known_person2_encoding = face_recognition.face_encodings(rgb_img2)
known_person3_encoding = face_recognition.face_encodings(rgb_img3)
# Generate face encodings for each known person
# known_person1_encoding = face_recognition.face_encodings(known_person1_image)
# known_person2_encoding = face_recognition.face_encodings(known_person2_image)
# known_person3_encoding = face_recognition.face_encodings(known_person3_image)

# Append the encodings and names to the lists
known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)

known_face_names.append("Madhu")
known_face_names.append("Tarun")
known_face_names.append("Chotu")

# Initialize the webcam
video_capture = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Check if the frame was successfully captured
    if not ret:
        print("Failed to grab frame")
        break

    # Convert the image from BGR (OpenCV) to RGB (face_recognition)
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Find all face locations in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)

    # Find face encodings for each face found in the frame
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If a match is found, set the name of the matched face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face and label with the name
        cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv.putText(frame, name, (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), thickness=2)

    # Display the resulting frame
    cv.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
video_capture.release()
cv.destroyAllWindows()
