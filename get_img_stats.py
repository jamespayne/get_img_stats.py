#!/usr/bin/env python

"""Find the height of an online image with different libraries and methods.
Benchmark the results based on connection speed and the server where the
resource is located.

Example: `python img_stats.py http://somedomain.com 1`

1. Using Pillow, StringIO and requests libraries.
See https://stackoverflow.com/a/25350894

All benchmarks don't currently include the time to import the required
libraries. I'll add those later. You'll need to pip install the requirements
manually atm.
"""

import argparse
import time

class ImageStats(object):
    """ImageStats object which returns the stats of an online image relevant
    to your connection and where you downloaded it from. Currently only reports
    image height and time to load."""

    def __init__(self, url):
        self.url = url

    def method(self, method):
        """ImageStats.method() chooses which method to use when getting the
        stats and returns the results for printing."""

        if method == 1:
            """See https://stackoverflow.com/a/12020866"""
            from PIL import Image
            from StringIO import StringIO
            import requests
            start_time = time.time()
            response = requests.get(self.url)
            img_height = str(Image.open(StringIO(response.content)).size[1])
            end_time = str(time.time() - start_time)
            return "Image Height: " + img_height + "px", \
                   "Execution time: " + end_time + " seconds"


def main():
    """main() prints the image stats based on the method you choose."""

    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("url")
    parser.add_argument("method")
    args = parser.parse_args()
    stats = ImageStats(args.url).method(int(args.method))
    print stats


if __name__ == "__main__":
    main()
