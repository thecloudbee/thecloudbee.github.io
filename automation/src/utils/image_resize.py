import sys

from PIL import Image
import PIL
import os
import glob


# https://sempioneer.com/python-for-seo/how-to-compress-images-in-python/
def compress_images(directory):
    os.chdir(directory)
    files = os.listdir()
    images = [file for file in files if file.endswith(('jpg', 'png'))]

    for image in images:
        img = Image.open(image)
        x, y = img.size
        print(f'Initial image: {image} with size: {x}, {y}')
        if x < 200 or y < 200:
            print(f'Skipping compressing for image: {image}. Reason, too small.')
            continue
        base_width = 1200
        wpercent = (base_width / float(img.size[0]))
        height = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((base_width, height), Image.ANTIALIAS)
        print(f'Final image: {image} with size: {base_width}, {height}')

        # image_size_in_kb = int(sys.getsizeof(img.tobytes())/100)
        # quality = int(100 * 100 / image_size_in_kb)

        img.save(image, optimize=True, quality=50)


compress_images('/Users/amroj/IdeaProjects/thecloudbee.github.io/assets/images/2021-01-01')
