import os
import subprocess


def convert_image() -> None:
    path = input("Enter full path to your folder with images: ")

    # allowed extensions for conversion
    allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif']

    # if empty, use 80
    try:
        quality = int(
            input("Enter compression quality in numbers from 1 to 100: ")) or 80
    except ValueError:
        print("This is not a numeric value")
        exit(1)

    # you cant trust users :D
    if quality not in range(1, 101):
        raise Exception("Sorry, allowed numbers only between 1 - 100")

    # if this attribute is empty, use the same path
    destination_path = input("Destination path: ") or path

    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print("Wrong file or file path")
        exit(1)

    # you cant trust users, again :D
    if path[-1] != '/':
        path = path + '/'

    for file in files:
        divide_file = os.path.splitext(file)
        ext, prefix = divide_file[1], divide_file[0]
        full_path = path + file
        if ext.lower() in allowed_extensions:
            temp = prefix
            try:
                bashCommand = "cwebp -q " + \
                    str(quality) + " " + full_path + " -o " + \
                    destination_path + temp + ".webp"
                process = subprocess.Popen(
                    bashCommand.split(), stdout=subprocess.PIPE)
                _, error = process.communicate()
                if error:
                    print("Conversion failed")
            except FileNotFoundError:
                print("Wrong file")
            except SyntaxError:
                print("Invalid file")

    print("---- Conversion DONE ----")
    exit(1)


convert_image()
