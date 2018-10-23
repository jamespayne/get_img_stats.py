# get_img_stats.py

Find the height of an online image with different libraries and methods.
Benchmark the results based on connection speed and the server where the
resorce is located.

Example: `python img_stats.py http://somedomain.com 1`

1. Using Pillow, StringIO and requests libraries.
See https://stackoverflow.com/a/25350894

All benchmarks don't currently include the time to import the required
libraries. I'll add those later. You'll need to pip install the requirements
manually atm.
