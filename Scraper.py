__author__ = 'Michael'

import urllib.request
import os

home = os.getcwd()

for i in range(1, 6):
    os.makedirs(os.getcwd() + "/Volume " + str(i))
    os.chdir(os.getcwd() + "/Volume " + str(i))

    url = "http://carciphona.com/_pages//" + str(i) + "/cover.jpg"

    urllib.request.urlretrieve(url, "cover" + str(i) + ".jpg")

    print("Cover " + str(i) + " retrieved!")

    for j in range(1, 200):
        url = "http://carciphona.com/_pages//" + str(i) + "/" + str(j).zfill(3) + ".jpg"
        path = str(j).zfill(3) + ".jpg"

        urllib.request.urlretrieve(url, path)

        if os.path.getsize(path) < 25 * 1024:
            os.remove(path)
            print("Page " + str(j) + " of chapter " + str(i) + " does not exist, temp file deleted!")
        else:
            print("Page " + str(j) + " of chapter " + str(i) + " retrieved!")

    os.chdir(home)