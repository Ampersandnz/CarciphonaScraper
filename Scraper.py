__author__ = 'Michael'
# Thanks to http://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python

import urllib.request
import os
from pathlib import Path
from multiprocessing.pool import Pool


def main():
    home = os.getcwd()
    for i in range(1, 6):
        download_dir = Path(os.getcwd() + "/Volume " + str(i))

        if not download_dir.exists():
            download_dir.mkdir()
        os.chdir(download_dir.name)

        cover_url = "http://carciphona.com/_pages//" + str(i) + "/000.jpg"
        download_file(cover_url)

        urls = []
        for j in range(1, 200):
            urls.append("http://carciphona.com/_pages//" + str(i) + "/" + str(j).zfill(3) + ".jpg")

        # 2x as many processes as I have processors for better performance on more powerful systems, and because I may
        # get more speedup by utilising the time spent waiting for the website to respond.
        # Might not actually help though.
        with Pool(12) as p:
            p.map(download_file, urls)

        os.chdir(home)


def download_file(url):
    filename = url.split("/")[-1]
    volume = url.split("/")[-2]
    urllib.request.urlretrieve(url, filename)

    if os.path.getsize(filename) < 25 * 1024:
        os.remove(filename)
        print("Page " + filename + " of volume " + volume + " does not exist, temp file removed.")
    else:
        print("Page " + filename + " of volume " + volume + " retrieved!")

if __name__ == "__main__":
    main()