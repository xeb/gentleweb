#!/bin/bash

# Firefox or geckodriver
wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux32.tar.gz
tar zxvf geckodriver*.tar.gz
rm -r geckodriver*.tar.gz
rm geckodriver.log


# Chrome
wget https://chromedriver.storage.googleapis.com/104.0.5112.79/chromedriver_linux64.zip
unzip chromedriver*.zip
rm -r chromedriver*.zip
