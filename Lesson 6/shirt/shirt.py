import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        read_file = sys.argv[1]
        write_file = sys.argv[2]
        if check_path(read_file, write_file) == True:
            try:
                with Image.open("shirt.png") as shirt, Image.open(read_file) as photo:
                    size = shirt.size
                    photo = ImageOps.fit(photo, size)
                    photo.paste(shirt, (0, 0), shirt)
                    photo.save(write_file)
            except FileNotFoundError:
                sys.exit(f"Input does not exist")

def check_path(read_file, write_file):
    read_path = os.path.splitext(read_file)[1].lower()
    write_path =os.path.splitext(write_file)[1].lower()
    valid_extensions = [".jpg", ".jpeg", ".png"]
    if read_path not in valid_extensions:
        sys.exit("Invalid input")
    elif write_path not in valid_extensions:
        sys.exit("Invalid output")
    elif read_path != write_path:
        sys.exit("Input and output have different extensions")
    else:
        return True

if __name__ == "__main__":
    main()
