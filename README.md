# get_img_stats.py

Find the height of an online image with different libraries and methods.
Benchmark the results based on connection speed and the server where the
resource is located.

This is a project I started because I wanted to understand how an image was downloaded from a URI.

Example: `python img_stats.py http://somedomain.com/img.jpg 1`

**Good Cases**

Hopefully coming soon

**Bad Cases** (where the whole image needs to be downloaded causing a significant overhead):

1. Using Pillow, StringIO and requests libraries.
See https://stackoverflow.com/a/25350894

All benchmarks don't currently include the time to import the required
libraries. I'll add those later. You'll need to pip install the requirements
manually atm.
