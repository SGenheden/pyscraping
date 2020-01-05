import glob
import os

from pyscraping.utils import write_html_view


def main():
    import sys

    filenames = glob.glob("*.jpg")
    if len(sys.argv) > 1 and sys.argv[1] == "-r":
        filenames += glob.glob("*/*.jpg")
    images = [(filename, filename) for filename in sorted(filenames)]
    html_filename = os.path.join(os.getcwd(), "view.html")
    write_html_view(html_filename, images, width=150)
