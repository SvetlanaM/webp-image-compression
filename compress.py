import os
import subprocess


def convert_image() -> None:
    path = input("Enter full path to your folder with images: ")

    # allowed extensions for conversion
    allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.heic']

    try:
        quality = int(
            input("Enter compression quality in numbers from 1 to 100: "))
    except ValueError:
        print("This is not a numeric value")
        exit(1)

    # you cant trust users :D
    if quality not in range(1, 101):
        raise Exception("Sorry, allowed numbers only between 1 - 100")

    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print("Wrong file or file path")
        exit(1)

    # you cant trust users, again :D
    if path[-1] != '/':
        path = path + '/'

    # if this attribute is empty, use the same path
    destination_path = dest if (dest := input(
        "Destination path: ") != '') else path

    # filter only images and nothing more
    filtered_files = filter(lambda file: os.path.splitext(file)[
                            1].lower() in allowed_extensions, files)

    for file in filtered_files:
        divide_file = os.path.splitext(file)
        file_name = divide_file[0]
        full_path = path + file
        try:
            bashCommand = "cwebp -q " + \
                str(quality) + " " + full_path + " -o " + \
                destination_path + file_name + ".webp"
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


convert_image()
