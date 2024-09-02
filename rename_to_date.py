import os
from PIL import Image, ExifTags
from datetime import datetime

# Path to the directory containing images
input_folder = './<<input_folder>>'
# Path to the directory where you want to save the processed images
output_folder = './<<output_folder>>'

# Create the output directory if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Function to read the date from the image metadata
def get_capture_date(image):
    try:
        for tag, value in image._getexif().items():
            if ExifTags.TAGS.get(tag) == 'DateTimeOriginal':
                return value
    except Exception as e:
        print(f"Could not read the date. Error: {e}")
    return None

i=1
# Processing each file in the directory
for filename in os.listdir(input_folder):
    print(i)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check if the file is an image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Reading the date from the image
        capture_date = get_capture_date(img)
        if capture_date:
            # Convert the date to the format yyyymmdd HHMMSS
            date_object = datetime.strptime(capture_date, '%Y:%m:%d %H:%M:%S')
            new_filename = f'IMG_{date_object.strftime("%Y%m%d")}_{date_object.strftime("%H%M%S")}.jpg'  # Add IMG_ before the date and time
            output_path = os.path.join(output_folder, new_filename)

            # Save the image to the new directory with the new name
            img.save(output_path)
            print(f"Saved: {output_path}")
        else:
            print(f"No date found for: {filename}")
    i=i+1
print("Processing completed!")
