Instruction for me from the future:: 

Download the required packages
In each script, update the "input_folder" and "output_folder" variables

1. Download `shape_predictor_68_face_landmarks.dat` (https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat) and put it in the same directory as scripts
2. Put directory with photos in the same directory as scripts
3. If photos need to be mirrored, run `mirror_photos.py`
4. If photos are in HEIC format, use https://pypi.org/project/heic-to-jpg/ to convert them to jpeg (usage example: `heic-to-jpg -s ./<<input_directory>>`)
5. If photos need to be renamed to contain info about creation date, run `rename_to_date.py`
6. If photos are ready to be aligned, run `photo_face_detection.py` 
