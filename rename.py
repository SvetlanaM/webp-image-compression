import os
import unicodedata as ud

path = input("Enter full path to your folder with images: ")
files = os.listdir(path)


def rename_image():

    for _, file in enumerate(files):
        new_file = ud.normalize('NFC', file)
        os.rename(os.path.join(path, new_file),  os.path.join(
            path, '_' + 'product_'.join([file.replace(" ", "_").replace(".jpg", ""), '.jpg']).lower()))


rename_image()
