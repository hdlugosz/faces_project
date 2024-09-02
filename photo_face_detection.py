# For converting heic->jpg: https://pypi.org/project/heic-to-jpg/ 
import cv2
import dlib
import numpy as np
import os
from imutils import face_utils

# Settings
input_folder = './<<input_folder>>'  # Path to the folder with images
output_folder = './<<output_folder>>'  # Path to the folder for processed images

# Create the output directory if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Loading the face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

# Function to align the image
def align_image(image, image_path):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    if len(faces) > 0:
        landmarks = predictor(gray, faces[0])
        landmarks_np = face_utils.shape_to_np(landmarks)

        left_eye = landmarks_np[36:42]  # Points for the left eye
        right_eye = landmarks_np[42:48]  # Points for the right eye

        # Calculating the center of the pupils for the left and right eye
        left_eye_center = np.mean(left_eye, axis=0).astype("float")
        right_eye_center = np.mean(right_eye, axis=0).astype("float")

        # Calculate the center of the eyes
        eyes_center = ((left_eye_center[0] + right_eye_center[0]) / 2.0,
                       (left_eye_center[1] + right_eye_center[1]) / 2.0)

        # Set desired eye positions based on the width of the image
        desired_eye_x_left = int(image.shape[1] * 0.40)  # Set X for the left eye
        desired_eye_x_right = int(image.shape[1] * 0.60)  # Set X for the right eye
        desired_eye_y = int(image.shape[0] * 0.40)  # Set Y for both eyes

        # Calculate the height difference between the eyes
        delta_y = right_eye_center[1] - left_eye_center[1]
        delta_x = right_eye_center[0] - left_eye_center[0]
        
        # Calculate the rotation angle
        angle = np.degrees(np.arctan2(delta_y, delta_x))

        # Calculate the distance between the eyes
        current_eye_distance = np.linalg.norm(right_eye_center - left_eye_center)
        desired_distance = desired_eye_x_right - desired_eye_x_left

        # Calculate the scale
        scale = desired_distance / current_eye_distance

        # Calculate the translation
        x_translation = (desired_eye_x_left + desired_eye_x_right) / 2 - eyes_center[0]
        y_translation = desired_eye_y - eyes_center[1]

        # Create the transformation matrix (with rotation and scaling)
        M = cv2.getRotationMatrix2D(eyes_center, angle, scale)  # Rotate by the calculated angle
        M[0, 2] += x_translation
        M[1, 2] += y_translation

        # Shift the image
        aligned_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

        return aligned_image
    else:
        print("Nie znaleziono twarzy na zdj: " + image_path)
    return image


i = 1
# Processing all images in the folder
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        print(i)
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        aligned_image = align_image(image, image_path)

        cv2.imwrite(os.path.join(output_folder, filename), aligned_image)
        i=i+1
print("Processing completed.")
