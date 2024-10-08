import cv2
import numpy as np

# Load haarcascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
    return faces

def blur_faces(frame, faces, blur_strength=15):
    if blur_strength % 2 == 0:
        blur_strength += 1
    if blur_strength <= 0:
        blur_strength = 1

    for (x, y, w, h) in faces:
        face_region = frame[y:y+h, x:x+w]
        blurred_face = cv2.GaussianBlur(face_region, (blur_strength, blur_strength), 0)
        frame[y:y+h, x:x+w] = blurred_face
    return frame

def pixelize_faces(frame, faces, pixel_size=10):
    for (x, y, w, h) in faces:
        face_region = frame[y:y+h, x:x+w]
        small = cv2.resize(face_region, (w // pixel_size, h // pixel_size), interpolation=cv2.INTER_LINEAR)
        pixelized_face = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
        frame[y:y+h, x:x+w] = pixelized_face
    return frame

def replace_faces_with_icon(frame, faces, icon_path):
    # Load the icon
    icon = cv2.imread(icon_path, cv2.IMREAD_UNCHANGED)

    if icon is None:
        print("Error: Icon could not be loaded.")
        return frame

    for (x, y, w, h) in faces:
        # Resize the icon to match the face dimensions
        icon_resized = cv2.resize(icon, (w, h))

        # If the icon has transparency (4 channels), handle blending
        if icon_resized.shape[2] == 4:
            alpha_icon = icon_resized[:, :, 3] / 255.0
            alpha_frame = 1.0 - alpha_icon

            for c in range(0, 3):  # Apply the first 3 channels (RGB) with blending
                frame[y:y+h, x:x+w, c] = (alpha_icon * icon_resized[:, :, c] +
                                          alpha_frame * frame[y:y+h, x:x+w, c])
        else:
            # No transparency, directly replace face with the icon
            frame[y:y+h, x:x+w] = icon_resized

    return frame

def process_image(image_path, method, blur_strength, icon_path=None):
    frame = cv2.imread(image_path)
    faces = detect_faces(frame)

    if method == 'Blur':
        frame = blur_faces(frame, faces, blur_strength)
    elif method == 'Pixelize':
        frame = pixelize_faces(frame, faces)
    elif method == 'Replace with Icon' and icon_path:
        frame = replace_faces_with_icon(frame, faces, icon_path)

    cv2.imshow('Processed Image', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_video(video_path, method, blur_strength, icon_path):
    vid = cv2.VideoCapture(video_path)

    while True:
        ret, frame = vid.read()
        if not ret:
            break

        faces = detect_faces(frame)

        if method == 'Blur':
            frame = blur_faces(frame, faces, blur_strength)
        elif method == 'Pixelize':
            frame = pixelize_faces(frame, faces)
        elif method == 'Replace with Icon' and icon_path:
            frame = replace_faces_with_icon(frame, faces, icon_path)

        cv2.imshow('Processed Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

def stream_from_camera(method, blur_strength, icon_path):
    vid = cv2.VideoCapture(0)  # Use the default camera
    
    while True:
        ret, frame = vid.read()
        if not ret:
            break

        faces = detect_faces(frame)

        if method == 'Blur':
            frame = blur_faces(frame, faces, blur_strength)
        elif method == 'Pixelize':
            frame = pixelize_faces(frame, faces)
        elif method == 'Replace with Icon' and icon_path:
            frame = replace_faces_with_icon(frame, faces, icon_path)

        cv2.imshow('Camera Stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()
