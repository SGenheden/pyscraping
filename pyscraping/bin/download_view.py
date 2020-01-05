import tempfile
import os
import sys
from concurrent.futures import ThreadPoolExecutor

from pyscraping.utils import links_from_view, download_url, image_nr


def main():
    view_filename = sys.argv[1]
    if len(sys.argv) == 3:
        dirpath = os.path.join(sys.argv[2], os.path.basename(view_filename)[:-5])
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
    else:
        dirpath = tempfile.mkdtemp()

    path_tuples = []
    for i, url in enumerate(links_from_view(view_filename), 1):
        path_tuples.append((url, os.path.join(dirpath, f"image{image_nr(i)}.jpg")))

    with ThreadPoolExecutor(10) as executor:
        res = executor.map(download_url, path_tuples)

    print(f"Saved {len(list(res))} images to {dirpath}")
