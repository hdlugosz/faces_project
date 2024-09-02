import os
from PIL import Image

# Ścieżka do katalogu ze zdjęciami
input_folder = './<<input_folder>>'
# Ścieżka do katalogu, w którym chcesz zapisać odbicia lustrzane
output_folder = './<<output_folder>>'

# Utwórz katalog wyjściowy, jeśli nie istnieje
os.makedirs(output_folder, exist_ok=True)

# Przetwarzanie każdego pliku w katalogu
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Sprawdź, czy plik jest obrazem
        # Ładowanie obrazu
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # Odwracanie obrazu lustrzanie
        img_mirrored = img.transpose(Image.FLIP_LEFT_RIGHT)
        
        # Zapisz odwrócony obraz w nowym katalogu
        output_path = os.path.join(output_folder, filename)
        img_mirrored.save(output_path)

print("Przetwarzanie zakończone!")