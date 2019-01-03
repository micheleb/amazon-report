# amazon-report
Get your CSV reports back from amazon!

# why
US users have a nice 'Download report' feature that lets them get a CSV with
all items they bought on amazon.com, but unfortunately, the feature
is not there (yet?) everywhere in the world. At least it doesn't work in
Germany, or maybe only for my account. He. This script tries to bring the 
feature to all amazon users.

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

# shakiness ensues

Unfortunately replicating the `POST` calls that the website makes to Amazon's
servers is no longer a trivial task, as the JS is using some sorcery to encode
several headers/parameters that let requests go through. Since I wanted to
play with Selenium anyway, I went for that instead. However, the script
obviously heavily relies on the web page structure at the time I wrote the
script for my own needs, so it can easily break as soon as they change their
layout. Try and open an issue, if you're reading this and this happens to you!

[1]: https://github.com/mozilla/geckodriver/releases
[2]: https://sites.google.com/a/chromium.org/chromedriver/downloads
