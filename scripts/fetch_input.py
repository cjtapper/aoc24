import argparse
import os
import urllib.request


def day(s: str) -> int:
    day = int(s)

    if not 1 <= day <= 25:
        raise ValueError("day must be in range [1,25]")

    return day


parser = argparse.ArgumentParser()
parser.add_argument("day", type=day)
args = parser.parse_args()

session_cookie = os.environ["AOC_SESSION_COOKIE"]

request = urllib.request.Request(
    url=f"https://adventofcode.com/2024/day/{args.day}/input",
    headers={"Cookie": f"session={session_cookie}"},
)

with urllib.request.urlopen(request) as response:
    input_data = response.read().decode("utf-8")

print(input_data)
