import os
from PIL import Image

# CONFIGURATION
INPUT_FOLDER = r'C:\Users\2018553\Pictures\JAIBB' # Folder containing original images
OUTPUT_FOLDER = r'C:\Users\2018553\Pictures\JAIBB\output' # Folder to save processed images
MAX_SIZE_KB = 512 # Maximum file size in KB
TARGET_WIDTH = 400
TARGET_HEIGHT = 520
FORMATS_ALLOWED = ['.jpg', '.jpeg', '.png']

# Create output folder if not exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def compress_image(image, output_path, format, quality=85):
    """Compress image recursively until it's under MAX_SIZE_KB"""
    while True:
        image.save(output_path, format=format, quality=quality, optimize=True)
        size_kb = os.path.getsize(output_path) / 1024
        if size_kb <= MAX_SIZE_KB or quality < 20:
            break
        quality -= 5 # Reduce quality step by step

def process_images():
    print("hi")
    for filename in os.listdir(INPUT_FOLDER):
        file_ext = os.path.splitext(filename)[-1].lower()
        if file_ext not in FORMATS_ALLOWED:
            continue

        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, os.path.splitext(filename)[0] + '.jpg')

        try:
            with Image.open(input_path) as img:
                # Convert to RGB if not already (important for JPEG)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize
                img = img.resize((TARGET_WIDTH, TARGET_HEIGHT))

                # Save as compressed JPEG
                compress_image(img, output_path, format='JPEG')
                print(f"Processed: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")


process_images()