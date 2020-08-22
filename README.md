# Crawl_IMDb_top_250
This software will use `Beautiful Soup 4`, `requests` and `pandas` library to automatically parse the HTML code of the top 250 IMDb movies page with the link https://www.imdb.com/chart/top/, and divide the information of these movies into: `Rank`, `Movie Names`, `Links`, `Rating Values`, `Directors`, `Writers`, `Stars`, `Casts`, `Genres`, `Certificate`, `Country`, `Language`, `Release Date`, `Filming Locations`, `Budget`, `Opening Weekend USA`, `Gross USA`, `Cumulative Worldwide Gross`, `Runtime`. Make as a CSV file

Welcome to use my software to study or research. If you don't want to spend time crawling the webpage again, you can use the ready-made CSV file as the analysis material.

# How to install
Clone `scraping.py` from git hub

`Requisites`: Need Python 3.0 or later to run software

`Install Beautiful Soup 4`: `pip install beautifulsoup4` (Some `pip` may be named `pip3` respectively if you’re using Python 3)
recent version of Debian or Ubuntu Linux : `apt-get install python3-bs4`

`Install requests`: `pip install requests` (Some `pip` may be named `pip3` respectively if you’re using Python 3)

`Install pandas`: `sudo apt-get install python3-pandas` (pip might cause errors)

# License Information
This repository has a general MIT License with some addtional conditons. Please review the license before using any segments of the repository.
