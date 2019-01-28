import argparse
import os
import pathlib
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('times', type=pathlib.Path)
    parser.add_argument('clip', type=pathlib.Path)
    args = parser.parse_args()
    
    times = get_times(args.times)

    for i, (start, end) in enumerate(times):
        out = f'{args.clip.stem}_{i:02}{args.clip.suffix}'
        subprocess.run([
            'ffmpeg', '-ss', start, '-to', end,
            '-i', os.fspath(args.clip), out])


def get_times(times_file):
    data = times_file.read_text()
    lines = data.split()
    return [l.strip().split('|') for l in lines]


if __name__ == '__main__':
    sys.exit(main())

