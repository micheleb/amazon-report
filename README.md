# amazon-report
Get your CSV reports back from amazon!

# why
US users have a nice 'Download report' feature that lets them get a CSV with
the list of all items they bouth on amazon.com, but unfortunately, the feature
is not there (yet?) everywhere in the world. At least it doesn't work in
Germany, or maybe only for my account. This script tries to bring the feature
to all amazon users.

# running it
You need to install the Selenium Web Driver for either [Firefox][1] or
[Chrome/Chromium][2], and make sure that the executable is in your `PATH`
environment variable. Then, I suggest creating a virtualenv for python, but of
course it's optional. To install all dependencies, run:

    pip install -r requirements.txt

And finally, run:

    python amazon-report.py

The script will ask for the URL to use (without http:// or https://), the
driver to use (according to what you installed), and your credentials to fetch
your data. They're obviously not stored anywhere, see the code for yourself!

[1]: https://github.com/mozilla/geckodriver/releases
[2]: https://sites.google.com/a/chromium.org/chromedriver/downloads
