import os
import time
import sys

destination = input("Enter Path to the destination directry ")
src = input("Enter Path to the source directry ")


def check(filename):
    for file_name in os.listdir(destination):
        if filename == file_name:
            return True
    else:
        return False


def rename(filename, n):
    renamed_file = filename
    chars = list(renamed_file)
    for i in range(len(chars)):
        if chars[i] == ".":
            chars[i] = str(n) + "."
    return "".join(chars)


try:
    while True:
        time.sleep(3)
        for filename in os.listdir(src):
            r = 1
            renamed_file = filename
            while check(renamed_file):
                renamed_file = rename(renamed_file, r)
                r += 1
            os.rename(src + "\\" + filename, destination + "\\" + renamed_file)
except KeyboardInterrupt:
    sys.exit()
