# Python Web Scraper Tutorial

## Introduction
This repository contains the Python script for a basic web scraper, as demonstrated in the article "**Build Your First Web Scraper with Python and BeautifulSoup**". The script is designed for beginners to understand the fundamentals of web scraping using Python.

## Full Article
For a comprehensive guide, including the step-by-step process, challenges, and ethical considerations of web scraping, visit the full article:
[Build Your First Web Scraper with Python and BeautifulSoup](https://nemanjatanaskovic.com/build-your-first-web-scraper-with-python-and-beautifulsoup/)

## Requirements
- Python 3.10.11 or later
- pip 23.0.1 or later

## Installing Python and pip
Ensure you have Python and pip installed on your computer. Here's how to install them on different operating systems:

### macOS
1. **Install Python**: Download from the official Python website or use Homebrew with `brew install python@3.10`.
2. **Install Pip**: Included by default from Python 3.4 onwards. Update with `python3 -m pip install --upgrade pip`.

### Windows
1. **Install Python**: Download from the Python website and ensure to check “Add Python 3.10 to PATH” during installation.
2. **Install Pip**: Comes pre-installed. Update with `python -m pip install --upgrade pip` in Command Prompt.

### Linux
1. **Install Python**: Usually pre-installed or use `sudo apt-get install python3.10` for Ubuntu.
2. **Install Pip**: Install with `sudo apt install python3-pip` and upgrade with `python3 -m pip install --upgrade pip`.

## Setting Up a Python Virtual Environment
A Python virtual environment is recommended for managing dependencies. Here's how to set one up:

1. **Install `virtualenv`**:
   ```bash
   pip install virtualenv
2. **Create a Virtual Environment**:
   3. Navigate to your project directory and run:
    ```bash
   virtualenv venv
3. **Activate the Virtual Environment:**
   4. On macOS and Linux:
   ```bash
   source venv/bin/activate
   ```
   5. **On Windows:**
   ```bash
   .\venv\Scripts\activate

## Installation
Install the required Python libraries within your virtual environment using the following commands:
```bash
pip install requests
pip install beautifulsoup4
```