#!/usr/bin/env python3
from os import get_terminal_size
from re import match

import click
from PIL import Image, ImageSequence
from requests import get
from sty import bg, fg, rs


def get_pixel_rows(line: int, im: Image.Image):
    data = im.getdata()
    w = im.width

    for i in range(w):
        yield data[line*w+i], data[(line+1)*w+i]


def render_RGBA_img(im: Image.Image, h: int):
    lines = []
    for lineno in range(0, h-1, 2):
        line = ""
        for pixel in get_pixel_rows(lineno, im):
            if pixel[0][3] == 0 and pixel[1][3] == 0:
                line += rs.all+' '
            elif pixel[1][3] == 0:
                line += rs.bg+fg(*pixel[0][:3])+'▀'
            else:
                line += bg(*pixel[0][:3])+fg(*pixel[1][:3])+'▄'

        line += rs.all
        lines.append(line)

    print('\n'.join(lines))


@click.command()
@click.argument('file_name')
@click.option('-a', '--ascii', 'ascii', is_flag=True, help='Whether to show as ascii art')
@click.option('-r', '--rotate', 'rotate', type=float)
def ascii_art(file_name: str, ascii: bool, rotate: float):
    if match(r'http(s)?://', file_name):
        try:
            r = get(file_name, stream=True)
            if r.status_code != 200:
                raise
            im = Image.open(r.raw)
            r.close()
        except:
            print("Error: Image could not be loaded")
            exit(1)
    else:
        try:
            im = Image.open(file_name)
        except:
            print("Error: Image could not be loaded")
            exit(1)

    if rotate is not None:
        im = im.rotate(rotate)

    iw, ih = im.size
    ratio = iw/ih

    h = get_terminal_size().lines
    w = round(h*ratio)

    if not ascii:
        h = h*2
        w = w*2
    else:
        w = w*2

    try:
        im = im.resize((w, h))
    except ValueError:
        print("Error: Wrong image size!\n")
        exit(1)

    if ascii:
        characters = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
        im = im.convert("L")
        pixels = im.getdata()

        res = ""
        for i, pixel in enumerate(pixels):
            if i % w == 0:
                res += "\n"

            res += characters[
                int(pixel/256*len(characters))
            ]
        print(res)

    else:
        im = im.convert('RGBA')

        render_RGBA_img(im, h)


if __name__ == '__main__':
    ascii_art()
