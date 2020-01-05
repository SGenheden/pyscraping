import glob
import os
import subprocess

import requests
from bs4 import BeautifulSoup


def download_url(path_input):
    url, filename = path_input
    resp = requests.get(url)
    with open(filename, "wb") as fileobj:
        fileobj.write(resp.content)


def image_nr(index_):
    if index_ < 10:
        return "00" + str(index_)
    elif index_ < 100:
        return "0" + str(index_)
    return str(index_)


def links_from_view(filename):
    with open(filename, "r") as fileobj:
        soup = BeautifulSoup(fileobj.read(), "html.parser")
    return [link.get("href") for link in soup.find_all("a")]


def write_html_view(
    filename, images, width=None, height=None, open_in_safari=True, ncols=5
):
    height_str = f'height="{height}"' if height else ""
    width_str = f'width="{width}"' if width else ""
    with open(filename, "w") as fileobj:
        fileobj.write("<html>\n<body>\n<table>\n")
        fileobj.write("<tr>\n")
        for i, (preview_path, full_path) in enumerate(images, 1):
            img_str = " ".join([height_str, width_str, f'src="{preview_path}"'])
            fileobj.write(
                f'<td><a href="{full_path}" target="_blank"><img {img_str}></a></td>\n'
            )
            if i % ncols == 0:
                fileobj.write("</tr>\n<tr>")
        fileobj.write("</tr>\n</body>\n</html>")
    if open_in_safari:
        subprocess.call(f"open -a safari file://{filename}", shell=True)
