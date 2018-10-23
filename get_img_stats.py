#!/usr/bin/env python

"""Find the height of an online image with different libraries and methods.
Benchmark the results based on the server where the resource is.

Example: `python img_stats.py http://somedomain.com 1`

1. Using Pillow, StringIO and requests libraries.
See https://stackoverflow.com/a/25350894

All benchmarks don't currently include the time to import the required
libraries. I'll add those later. You'll need to pip install the requirements
manually atm.
"""

import argparse
import time

__author__ = "Jimmy Payne"

class ImageStats(object):
    """ImageStats object which returns the stats of an online image relevant
    to where you downloaded it from. Currently only reports image Height
    and time to load."""

    def __init__(self, url):
        self.url = url

    def method(self, method):
        """ImageStats.method() returns the image stats and a benchmark
        time from the relevant server"""

        if method == 1:
            """See https://stackoverflow.com/a/12020866"""
            from PIL import Image
            from StringIO import StringIO
            import requests
            start_time = time.time()
            response = requests.get(self.url)
            img_height = Image.open(StringIO(response.content)).size[1]
            end_time = time.time() - start_time
            return "Image Height: " + str(img_height) + "px", \
                   "Execution time: " + str(end_time) + " seconds"


def main():
    """main() returns the image stats based on the method you choose."""

    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("url")
    parser.add_argument("method")
    args = parser.parse_args()
    stats = ImageStats(args.url).method(int(args.method))
    print stats


if __name__ == "__main__":
    main()
