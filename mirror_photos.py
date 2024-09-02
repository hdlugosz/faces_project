import os
from PIL import Image

# Path to the directory containing images
input_folder = './<<input_folder>>'
# Path to the directory where you want to save mirrored images
output_folder = './<<output_folder>>'

# Create the output directory if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Processing each file in the directory
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check if the file is an image
        # Loading the image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # Flipping the image horizontally
        img_mirrored = img.transpose(Image.FLIP_LEFT_RIGHT)
        
        # Save the mirrored image in the new directory
        output_path = os.path.join(output_folder, filename)
        img_mirrored.save(output_path)

print("Processing completed!")
