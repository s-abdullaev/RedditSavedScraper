# Selenium-based Reddit Saved Urls Scraper

This is a small script for scraping saved urls and posts in your reddit profile. 

### Usage:

1. Install [Selenium](http://www.seleniumhq.org/download/) and [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/) on your computer.
2. Add to PATH environment variable the location of your Chrome Driver.
3. Set variables `username` and `pwd` in `reddit_saved_links.py` with your own reddit login and password
4. Run `reddit_saved_links.py` and watch Selenium driving your Chrome browser to scrape all data. The script generate `saved_link.json` file where you have all your data in a searchable format.