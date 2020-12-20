import os

from PIL import Image


# https://sempioneer.com/python-for-seo/how-to-compress-images-in-python/
def resize_images(directory):
    os.chdir(directory)
    files = os.listdir()
    images = [file for file in files if file.endswith(('jpg', 'png'))]

    for image in images:
        img = Image.open(image)
        x, y = img.size
        print(f'Initial image: {image} with size: {x}, {y}')
        if x < 200 or y < 200:
            print(f'#thecloudbee Skipping resize for image: {image}. Reason, too small.')
            continue
        elif x == 1200:
            print(f'#thecloudbee Skipping resize for image: {image}. Reason, already in-size.')
            continue
        base_width = 1200
        wpercent = (base_width / float(img.size[0]))
        height = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((base_width, height), Image.ANTIALIAS)
        print(f'#thecloudbee Final image: {image} with size: {base_width}, {height}')

        img.save(image, optimize=True, quality=80)


def resize_recursive(parent_directory):
    print(f'Current directory: {os.getcwd()}')
    print(f'#thecloudbee Starting process of image resize')
    for i in os.scandir(parent_directory):
        if i.is_dir():
            print(f'Processing folder: {i.path}')
            resize_images(i.path)
    print(f'#thecloudbee Ending process of image resize')


resize_recursive('../../../assets/images/')
