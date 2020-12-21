#!/usr/bin/env python3
# Based on https://geoffruddock.com/bulk-makeavif-x265-with-ffmpeg/

import os
import pathlib
import sys
from shutil import which
from subprocess import run
from typing import Iterable

import click

__version__ = '0.2.0'
SUPPORTED_FORMATS = ["jpg", "jpeg", "png", "y4m"]


# Ported from: https://github.com/victordomingos/optimize-images
def search_files(dirpath: str, recursive: bool) -> Iterable[str]:
    if recursive:
        for root, dirs, files in os.walk(dirpath):
            for f in files:
                if not os.path.isfile(os.path.join(root, f)):
                    continue
                extension = os.path.splitext(f)[1][1:]
                if extension.lower() in SUPPORTED_FORMATS:
                    yield os.path.join(root, f)
    else:
        with os.scandir(dirpath) as directory:
            for f in directory:
                if not os.path.isfile(os.path.normpath(f)):
                    continue
                extension = os.path.splitext(f)[1][1:]
                if extension.lower() in SUPPORTED_FORMATS:
                    yield os.path.normpath(f)


@click.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('-r', '--recursive', is_flag=True, help='Recursive')
@click.option('-s', '--speed', default='7', help='Speed: 1 is fastest, 8 is best quality')
@click.option('-c', '--codec', default='aom', help='Codec: aom (default) or svt (experimental)')
def main(directory, recursive=False, speed='7', codec='aom'):
    if which('avifenc') is None:
        print('avifenc not found')
        exit(1)
    total = 0
    num = 0
    jobs = len(os.sched_getaffinity(0)) - 1

    if recursive:
        print('Processing recursively starting from', directory)
        recursive = True
    else:
        print('Processing non-recursively starting from', directory)
        recursive = False

    if not os.access(directory, os.W_OK) or not os.path.exists(directory):
        print('No such directory or not writable')
        sys.exit(1)

    for filepath in search_files(str(directory), recursive=recursive):
        fp = pathlib.PurePath(filepath)
        newpath = fp.parent.joinpath(fp.stem + '.' + 'avif')
        convert_cmd = f'avifenc -j {jobs} -c {codec} -s {speed} {fp} -o {newpath}'
        conversion_return_code = run(convert_cmd, shell=True).returncode
        if conversion_return_code == 0:
            saved = os.path.getsize(fp) - os.path.getsize(newpath)
            total += saved
            num += 1
            print(newpath, 'ready, saved', round(saved / 1024), 'KB')
        else:
            print(fp, 'error')
    print('Total saved', round(total / 1024 / 1024), 'MB in', num, 'files')


if __name__ == '__main__':
    main()
