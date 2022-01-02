from PIL import Image
import os
import subprocess

path = input("Enter full path to your folder with images: ")
files = os.listdir(path)
allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif']

for file in files:
    ext = os.path.splitext(file)[1]
    full_path = path + file
    try:
        if ext.lower() in allowed_extensions:
            temp = os.path.splitext(file)[0]
            bashCommand = "cwebp -q 100 " +  full_path + " -o " + temp + ".webp"
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
    except FileNotFoundError:
        print("Wrong file or file path")
