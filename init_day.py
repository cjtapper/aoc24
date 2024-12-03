# copy template folder to new day
# fix the link in the top of the file
# download input

import string
import argparse
import shutil


def day(s: str) -> int:
    day = int(s)

    if not 1 <= day <= 25:
        raise ValueError("day must be in range [1,25]")

    return day


def pycache(dir, files):
    return ["__pycache__"] if "__pycache__" in files else []


parser = argparse.ArgumentParser()
parser.add_argument("day", type=day)
args = parser.parse_args()

shutil.copytree(src="./template", dst=f"day{args.day:02}", ignore=pycache)

with open(f"./day{args.day:02}/part1.py", "r") as file:
    contents = file.read()

template = string.Template(contents)
updated_contents = template.substitute(DAY=args.day)

with open(f"./day{args.day:02}/part1.py", "w") as file:
    file.write(updated_contents)



raise SystemExit(0)
