from PIL import Image
import os
import subprocess


path = input("Enter full path to your folder with images: ")
allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif']

try:
    quality = int(input("Enter compression quality in numbers from 1 to 100: " or "80"))
except ValueError:
    print("This is not a numeric value")
    exit(1)

try:
    files = os.listdir(path)
except FileNotFoundError:
    print("Wrong file or file path1")
    exit(1)


for file in files:
    ext = os.path.splitext(file)[1]
    full_path = path + file
    if ext.lower() in allowed_extensions:
        temp = os.path.splitext(file)[0]
        bashCommand = "cwebp -q " + str(quality) + " " + full_path + " -o " + path + temp + ".webp"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    
print("---- Conversion DONE ----")
exit(1)
    
