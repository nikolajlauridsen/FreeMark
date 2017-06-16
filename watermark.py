from PIL import Image
import os

INPUT_DIR = "images"
OUTPUT_DIR = "watermarked_images"
WATERMARK_FILE = "molex.png"
# The watermark will take up 15% of the horizontal space
LANDSCAPE_SCALE_FACTOR = 0.15
PORTRAIT_SCALE_FACTOR = 0.08
EQUAL_SCALE_FACTOR = 0.25
# Padding TODO: Make fluid
PADX = 20
PADY = 5

os.makedirs(OUTPUT_DIR, exist_ok=True)

watermark = Image.open(WATERMARK_FILE)
watermark_ratio = watermark.size[0]/watermark.size[1]

image_paths = os.listdir(INPUT_DIR)

for image_path in image_paths:
    try:
        image = Image.open(os.path.join(INPUT_DIR, image_path))
    except OSError:
        print("Bad image, skipping")
        continue

    image_width, image_height = image.size
    # Copy watermark and resize to better fit image
    if image_width > image_height:
        new_width = int(image_width * LANDSCAPE_SCALE_FACTOR)
        new_height = int(new_width / watermark_ratio)
    elif image_width < image_height:
        new_height = int(image_height * PORTRAIT_SCALE_FACTOR)
        new_width = int(new_height*watermark_ratio)
    else:
        new_width = int(image_width * EQUAL_SCALE_FACTOR)
        new_height = int(new_width / watermark_ratio)

    watermark_copy = watermark.copy().resize((new_width, new_height))
    print("New size: {}x{}".format(watermark_copy.size[0],
                                   watermark_copy.size[1]))

    # Calculate position for logo
    logo_x = image_width - watermark_copy.size[0] - PADX
    logo_y = image_height - watermark_copy.size[1] - PADY
    print("Putting logo at: {}x{}".format(logo_x, logo_y))
    # Paste the resized logo at the calculated position
    output_path = os.path.join(OUTPUT_DIR, image_path)
    print("Applying watermark and saving to to: " + output_path)
    try:
        image.paste(watermark_copy, box=(logo_x, logo_y), mask=watermark_copy)
    except ValueError:
        image.paste(watermark_copy, box=(logo_x, logo_y))
    image.save(output_path)
