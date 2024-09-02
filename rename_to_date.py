import os
from PIL import Image, ExifTags
from datetime import datetime

# Ścieżka do katalogu ze zdjęciami
input_folder = './<<input_folder>>'
# Ścieżka do katalogu, w którym chcesz zapisać przetworzone zdjęcia
output_folder = './<<output_folder>>'

# Utwórz katalog wyjściowy, jeśli nie istnieje
os.makedirs(output_folder, exist_ok=True)

# Funkcja do odczytywania daty z metadanych zdjęcia
def get_capture_date(image):
    try:
        for tag, value in image._getexif().items():
            if ExifTags.TAGS.get(tag) == 'DateTimeOriginal':
                return value
    except Exception as e:
        print(f"Nie można odczytać daty. Błąd: {e}")
    return None

i=1
# Przetwarzanie każdego pliku w katalogu
for filename in os.listdir(input_folder):
    print(i)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Sprawdź, czy plik jest obrazem
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Odczytując datę z zdjęcia
        capture_date = get_capture_date(img)
        if capture_date:
            # Konwertuj datę na format yyyymmdd HHMMSS
            date_object = datetime.strptime(capture_date, '%Y:%m:%d %H:%M:%S')
            new_filename = f'IMG_{date_object.strftime("%Y%m%d")}_{date_object.strftime("%H%M%S")}.jpg'  # Dodaj IMG_ przed datą i godziną
            output_path = os.path.join(output_folder, new_filename)

            # Zapisz zdjęcie do nowego katalogu z nową nazwą
            img.save(output_path)
            print(f"Zapisano: {output_path}")
        else:
            print(f"Nie znaleziono daty dla: {filename}")
    i=i+1
print("Przetwarzanie zakończone!")