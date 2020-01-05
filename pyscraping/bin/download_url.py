import sys
import os
from urllib.parse import urlparse

from pyscraping.utils import download_url


def main():
    url = sys.argv[1]
    if len(sys.argv) == 3:
        local_name = sys.argv[2]
    else:
        parts = urlparse(url)
        local_name = os.path.basename(parts.path)

    download_url((url, local_name))
    print(f"{url} downloaded to {local_name}")
